import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from colorama import init, Fore
import configparser
from datetime import datetime, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from selenium.common.exceptions import NoSuchElementException

# 設定ファイル読み込み
config = configparser.ConfigParser()
config.read('config.ini')

# Slack設定 (config.iniより取得)
SLACK_BOT_TOKEN = config['SLACK']['SLACK_BOT_TOKEN']
CHANNEL_ID = config['SLACK']['CHANNEL_ID']
client = WebClient(token=SLACK_BOT_TOKEN)

# パス設定 (config.iniより取得)
TEST_LOG_EXCEL = config['PATHS']['test_log_excel']
TEST_LOG_HTML = config['PATHS']['test_log_html']

# ブラウザ設定 (config.iniより取得)
BROWSER_TYPE = config['BROWSER']['browser']
IMPLICIT_WAIT = int(config['BROWSER']['implicit_wait'])

# colorama初期化
init(autoreset=True)

# 日付・時間関連変数
current_date = datetime.now().strftime("%Y/%m/%d")
today_date = datetime.now().day
tomorrow_date = datetime.now() + timedelta(days=1)
date_after_7_days = datetime.now() + timedelta(days=7)
end_day = date_after_7_days.day
is_next_month = datetime.now().month != date_after_7_days.month
this_week_monday = datetime.now() - timedelta(days=datetime.now().weekday())
current_hour = datetime.now().hour
current_minute = datetime.now().minute


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Slack共通API呼び出し関数
def slack_api_call(callable, *args, **kwargs):
    try:
        callable(*args, **kwargs)
        print(Fore.LIGHTGREEN_EX + "Slack操作が成功しました。")
    except SlackApiError as e:
        print(Fore.RED + f"Slack操作が失敗しました: {e.response['error']}")


# Slackメッセージ送信関数
def send_slack_message(message):
    slack_api_call(client.chat_postMessage, channel=CHANNEL_ID, text=message)


# Slackファイルアップロード関数
def upload_file_to_slack(file_path):
    slack_api_call(
        client.files_upload_v2,
        channel=CHANNEL_ID,
        file=file_path,
        title="テストレポート",
        initial_comment="✅ 自動テストが完了しました！HTMLレポートをご確認ください。"
    )


class SeleniumActions:
    def __init__(self, driver, test_cases_df):
        self.driver = driver
        self.local_test_cases_df = test_cases_df
        self.test_log = []
        self.step_counter = 1
        self.original_window = driver.current_window_handle

    def log_step(self, step_description, color, result):
        current_time = get_current_time()
        print(f"{self.step_counter}: " + Fore.YELLOW + f"[{current_time}] " + color + step_description)
        self.test_log.append({
            "No": self.step_counter,
            "Time": current_time,
            "Description": step_description,
            "Result": result
        })
        self.step_counter += 1
        time.sleep(2)

    def current_step(self, color=Fore.LIGHTGREEN_EX):
        try:
            step_description = self.local_test_cases_df.loc[self.local_test_cases_df['No'] == self.step_counter, 'case'].values[0]
            if pd.isna(step_description) or step_description == '':
                raise ValueError("ケース説明が空です。")
            self.log_step(step_description, color, "成功")
        except (IndexError, ValueError) as e:
            self.log_step(str(e), Fore.RED, "失敗")

    def enter_text(self, by, identifier, text):
        element = self.driver.find_element(by, identifier)
        element.send_keys(text)
        self.current_step()

    def click_element(self, by, identifier):
        element = self.driver.find_element(by, identifier)
        element.click()
        self.current_step()

    def double_click_element(self, by, identifier):
        element = self.driver.find_element(by, identifier)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.current_step()

    def move_to_element(self, by, identifier):
        element = self.driver.find_element(by, identifier)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.current_step()

    def press_key(self, by, identifier, key):
        element = self.driver.find_element(by, identifier)
        element.send_keys(key)
        self.current_step()

    def switch_to_original_tab(self):
        self.driver.switch_to.window(self.original_window)
        self.current_step()

    def generate_html_report(self, total_steps, success_steps, fail_steps):
        # テーブル行生成
        table_rows = ""
        for step in self.test_log:
            row_class = "success" if step["Result"] == "成功" else "fail"
            table_rows += f"""
            <tr class="{row_class}">
                <td>{step["No"]}</td>
                <td>{step["Time"]}</td>
                <td>{step["Description"]}</td>
                <td>{step["Result"]}</td>
            </tr>
            """

        # 根据测试结果确定test_result_class, test_result_text, fail_step_info
        if fail_steps > 0:
            test_result_class = "test-result-fail"
            test_result_text = "Fail"
            # 找出第一个失败步骤信息
            first_fail = next((item for item in self.test_log if item["Result"] != "成功"), None)
            if first_fail:
                fail_step_info = f"（No {first_fail['No']}: {first_fail['Description']} でエラー）"
            else:
                fail_step_info = ""
        else:
            test_result_class = "test-result-pass"
            test_result_text = "Pass"
            fail_step_info = ""

        # テンプレートファイルを読み込み
        with open('report_template.html', 'r', encoding='utf-8') as f:
            template = f.read()

        # プレースホルダを実際の値に置き換え
        html = template.format(
            report_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            report_env=config['DEFAULT']['url'],
            report_browser=BROWSER_TYPE,
            report_account=config['DEFAULT']['email'],
            total_steps=total_steps,
            success_steps=success_steps,
            fail_steps=fail_steps,
            table_rows=table_rows,
            test_result_class=test_result_class,
            test_result_text=test_result_text,
            fail_step_info=fail_step_info
        )

        return html

    def save_test_results(self):
        # テスト結果をExcelに保存
        test_log_df = pd.DataFrame(self.test_log)
        test_log_df.to_excel(TEST_LOG_EXCEL, index=False)
        print(Fore.LIGHTMAGENTA_EX + "テスト結果がExcelに保存されました。")

        # テスト結果統計
        total_steps = len(self.test_log)
        success_steps = sum(1 for item in self.test_log if item["Result"] == "成功")
        fail_steps = sum(1 for item in self.test_log if item["Result"] != "成功")

        # HTMLレポート生成
        html_report = self.generate_html_report(total_steps, success_steps, fail_steps)
        with open(TEST_LOG_HTML, 'w', encoding='utf-8') as f:
            f.write(html_report)
        print(Fore.LIGHTGREEN_EX + "HTMLレポートが生成されました。")

        # Slackへメッセージとファイル送信
        send_slack_message("✅ 自動テストが完了しました！HTMLレポートをアップロードします。")
        upload_file_to_slack(TEST_LOG_HTML)


def initialize_browser():
    if BROWSER_TYPE.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER_TYPE.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("config.iniに未対応のブラウザが指定されています。")
    driver.implicitly_wait(IMPLICIT_WAIT)
    return driver


def execute_test_case(driver, url, email, password, actions):
    try:
        # URLへアクセス
        driver.get(url)
        actions.current_step()

        # ブラウザ最大化
        driver.maximize_window()
        actions.current_step()

        # ログイン処理
        actions.enter_text(By.ID, "email", email)
        actions.enter_text(By.ID, "password", password)

        # ログインボタンをクリック
        actions.click_element(By.XPATH, "//button[contains(text(), 'ログイン')]")
        time.sleep(5)



    except NoSuchElementException as e:
        error_message = str(e).split("\n")[0]
        print(Fore.RED + f"テスト中に要素が見つかりませんでした: {error_message}")
        send_slack_message(f"❌ テスト中にエラーが発生しました: {error_message}")
        # 現在の step_counter を使用して、test_cases_df から失敗したステップの説明を取得します
        fail_step_no = actions.step_counter
        try:
            fail_step_desc = actions.local_test_cases_df.loc[actions.local_test_cases_df['No'] == fail_step_no, 'case'].values[0]
        except IndexError:
            fail_step_desc = "不明なステップ"
        # エラーメッセージと実際のエラーステップの説明を組み合わせてログに記録します
        actions.log_step(f"「{fail_step_no} - {fail_step_desc}」実行中に対象のボタンが見つからず、テストが失敗しました。", Fore.RED, "失敗")


    except Exception as e:
        error_message = str(e)
        print(Fore.RED + f"テスト中にエラーが発生しました: {error_message}")
        send_slack_message(f"❌ テスト中にエラーが発生しました: {error_message}")
        # 失敗したステップとして記録します
        actions.log_step("不明なエラーが発生し、テストが失敗しました。", Fore.RED, "失敗")

    finally:
        # 成功または失敗に関係なくレポートを生成します
        actions.save_test_results()


def main():
    driver = None
    actions = None
    try:
        driver = initialize_browser()
        actions = SeleniumActions(driver, pd.read_excel('test_cases.xlsx'))
        send_slack_message("🛠 自動テストを開始します...")

        execute_test_case(
            driver,
            config['DEFAULT']['url'],
            config['DEFAULT']['email'],
            config['DEFAULT']['password'],
            actions
        )

    except Exception as e:
        print(Fore.RED + f"テスト中にエラーが発生しました: {str(e)}")
        send_slack_message(f"❌ テスト中にエラーが発生しました: {str(e)}")
        # ここでエラーが発生した場合でも、アクションが初期化されている場合は、ここでレポートを生成する
        if actions:
            actions.save_test_results()
    finally:
        if driver:
            driver.quit()
            print(Fore.YELLOW + "ブラウザが正常に閉じられました。")


if __name__ == "__main__":
    main()
