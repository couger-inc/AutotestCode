import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from colorama import init, Fore
import configparser
from datetime import datetime, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from selenium.common.exceptions import NoSuchElementException

# 設定ファイルを読み込む
config = configparser.ConfigParser()
config.read('config.ini')

# Slack 設定（config.iniから取得）
SLACK_BOT_TOKEN = config['SLACK']['SLACK_BOT_TOKEN']
CHANNEL_ID = config['SLACK']['CHANNEL_ID']
client = WebClient(token=SLACK_BOT_TOKEN)

# パスの設定（config.iniから取得）
TEST_LOG_EXCEL = config['PATHS']['test_log_excel']
TEST_LOG_HTML = config['PATHS']['test_log_html']

# ブラウザ設定
BROWSER_TYPE = config['BROWSER']['browser']
IMPLICIT_WAIT = int(config['BROWSER']['implicit_wait'])

# coloramaを初期化
init(autoreset=True)

# 現在の日付と時間を管理する共通関数
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


# Slack共通API処理関数
def slack_api_call(callable, *args, **kwargs):
    try:
        callable(*args, **kwargs)
        print(Fore.LIGHTGREEN_EX + "Slack操作が成功しました！")
    except SlackApiError as e:
        print(Fore.RED + f"Slack操作が失敗: {e.response['error']}")


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
        initial_comment="✅ 自動テストが完了しました！HTMLレポートを確認してください。"
    )


# Seleniumアクション管理クラス
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

    def current_step(self, color=Fore.LIGHTGREEN_EX):
        try:
            step_description = self.local_test_cases_df.loc[self.local_test_cases_df['No'] == self.step_counter, 'case'].values[0]
            if pd.isna(step_description) or step_description == '':
                raise ValueError("case説明が空です。")
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

    def save_test_results(self):
        # テスト結果をExcelに保存
        test_log_df = pd.DataFrame(self.test_log)
        test_log_df.to_excel(TEST_LOG_EXCEL, index=False)
        print(Fore.LIGHTMAGENTA_EX + "テスト結果が保存されました。")

        # HTMLレポートを生成
        html_report = test_log_df.to_html()
        with open(TEST_LOG_HTML, 'w') as f:
            f.write(html_report)
        print(Fore.LIGHTGREEN_EX + "HTMLレポートが生成されました。")

        # Slackへメッセージとファイル送信
        send_slack_message("✅ 自動テストが完了しました！HTMLレポートをアップロードしています...")
        upload_file_to_slack(TEST_LOG_HTML)


def initialize_browser():
    if BROWSER_TYPE.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER_TYPE.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser specified in config.ini")
    driver.implicitly_wait(IMPLICIT_WAIT)
    return driver


def execute_test_case(driver, url, email, password, actions):
    try:
        # URLにアクセス
        driver.get(url)
        actions.current_step()

        # ブラウザを最大化
        driver.maximize_window()
        actions.current_step()

        # ログイン
        actions.enter_text(By.ID, "email", email)
        actions.enter_text(By.ID, "password", password)

        # 「ログイン」をクリック
        actions.click_element(By.XPATH, "//button[contains(text(), 'ログイン')]")
        time.sleep(5)

        # Weekly Point週「＜」ボタンを押す
        actions.click_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/button')

        # Weekly Point週「＞」ボタンを押す
        actions.click_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[3]/button')

        # 任意の項目をダブルクリックする
        actions.double_click_element(By.CSS_SELECTOR, "button.sc-ksZaOG.oOvMI.MuiButtonBase-root.sc-hAZoDl.fvaSUs.MuiIconButton-root.MuiIconButton-sizeMedium")

        # 元のブラウザーのタブに戻る
        actions.switch_to_original_tab()

        # 「新規ファイル」をクリック
        actions.click_element(By.XPATH, "//button[contains(., '新規ファイル')]")

        # 「キャンセル」をクリック
        actions.click_element(By.XPATH, "//button[contains(text(), 'キャンセル')]")

        # 「WPファイル」をクリック
        actions.click_element(By.XPATH, "//p[contains(text(), 'WPファイル')]")

        # Weekly Point週「＜」ボタンを押す
        actions.click_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/button')

        # Weekly Point週「＞」ボタンを押す
        actions.click_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[3]/button')

        # 任意の項目をダブルクリックする
        actions.double_click_element(By.CSS_SELECTOR, "button.sc-ksZaOG.oOvMI.MuiButtonBase-root.sc-hAZoDl.fvaSUs.MuiIconButton-root.MuiIconButton-sizeMedium")

        # 元のブラウザーのタブに戻る
        actions.switch_to_original_tab()

        # 「新規ファイル」ボタンをクリック
        actions.click_element(By.XPATH, "//button[contains(., '新規ファイル')]")

        # 「キャンセル」をクリック
        actions.click_element(By.XPATH, "//button[contains(text(), 'キャンセル')]")

        # 「新商品」をクリック
        actions.click_element(By.XPATH, "//p[contains(text(), '新商品')]")

        # Weekly Point週「＜」ボタンを押す
        actions.click_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/button')

        # Weekly Point週「＞」ボタンを押す
        actions.click_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[3]/button')

        # 任意の項目をダブルクリックする
        actions.double_click_element(By.CSS_SELECTOR, "button.sc-ksZaOG.oOvMI.MuiButtonBase-root.sc-hAZoDl.fvaSUs.MuiIconButton-root.MuiIconButton-sizeMedium")

        # 元のブラウザーのタブに戻る
        actions.switch_to_original_tab()

        # 「新規ファイル」をクリック
        actions.click_element(By.XPATH, "//button[contains(., '新規ファイル')]")

        # 「キャンセル」をクリック
        actions.click_element(By.XPATH, "//button[contains(text(), 'キャンセル')]")

        # 「データ登録」をクリック
        actions.click_element(By.XPATH, "//h3[contains(text(), 'データ登録')]")

        # 「WPデータ(管理者)」をクリック
        actions.click_element(By.XPATH, "//li[.//h3[contains(text(), 'WPデータ(管理者)')]]")

        # Weekly Point週「＜」ボタンを押す
        actions.click_element(By.CSS_SELECTOR, "button[type='button'] svg[data-testid='ArrowBackIosNewIcon']")

        # Weekly Point週「＞」ボタンを押す
        actions.click_element(By.CSS_SELECTOR, "button[type='button'] svg[data-testid='ArrowForwardIosIcon']")

        # もう一回Weekly Point週「＞」ボタンを押す
        actions.click_element(By.CSS_SELECTOR, "button[type='button'] svg[data-testid='ArrowForwardIosIcon']")

        # 各「発注地区」を選択
        regions = [
            "02 - 北陸", "03 - 関西", "04 - 岡山", "05 - 中部",
            "06 - 東海", "07 - 沖縄", "08 - 九州一", "09 - 九州二", "10 - 東北",
            "11 - 南九州", "12 - 福島", "13 - 北海道", "14 - ＴＯＭＯＮＹ", "15 - ＪＲ九州リテール",
            "16 - ＪＲ九州リテール２"
        ]
        for region in regions:
            actions.click_element(By.XPATH, "//button[@aria-label='Open' and @title='Open']")
            actions.click_element(By.XPATH, f"//li//*[contains(text(), '{region}')]")

        # 「新規登録」をクリック
        actions.click_element(By.XPATH, "//button[contains(., '新規登録')]")

        # 「施策名」を入力欄をクリック
        measure_name_element = driver.find_element(By.XPATH,
                                                   '//div[@class="sc-kYWVYA sc-eEOqmf fDeVho jzMarX MuiInputBase-root '
                                                   'MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth'
                                                   ' MuiInputBase-formControl"]/input[@type="text" and @class="sc-yeoIj '
                                                   'sc-lkwKjF kAIamR hpFbeN MuiInputBase-input MuiOutlinedInput-input"]')
        driver.execute_script("arguments[0].click();", measure_name_element)
        actions.current_step()

        # 「施策名」を入力
        driver.execute_script("arguments[0].value='12345';", measure_name_element)
        actions.current_step()

        # 「キャンセル」ボタンをクリック
        actions.click_element(By.XPATH, "//button[contains(text(), 'キャンセル')]")

        # 「新規登録」をクリック
        actions.click_element(By.XPATH, "//button[contains(., '新規登録')]")

        # 「展開開始日」の「日付を選択」ボタンをクリック
        actions.click_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div[5]/div/div[1]/div/div/div/div/div/button')

        # 「展開開始日」を選択
        actions.click_element(By.XPATH, f'//button[@role="gridcell" and text()="{today_date}"]')

        # 「展開開始日」/「時」の入力欄をクリック
        actions.click_element(By.XPATH, '(//input[@type="number" and @min="0" and @max="23" and @step="1"])[1]')

        # 「展開開始日」/「時」を入力
        driver.find_element(By.XPATH, '(//input[@type="number" and @min="0" and @max="23" and @step="1"])[1]').send_keys(str(current_hour))
        actions.current_step()

        # 「展開開始日」/「分」の入力欄をクリック
        actions.click_element(By.XPATH, '(//input[@type="number" and @min="0" and @max="59" and @step="1"])[1]')

        # 「展開開始日」/「分」を入力
        driver.find_element(By.XPATH, '(//input[@type="number" and @min="0" and @max="59" and @step="1"])[1]').send_keys(str(current_minute))
        actions.current_step()

        # 「展開終了日」の「日付を選択」ボタンをクリック
        actions.click_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div[6]/div/div[1]/div/div/div/div/div/button')

        # 「>」をクリック
        actions.click_element(By.XPATH, '//button[@aria-label="Next month" and @title="Next month"]')

        # 「<」をクリック
        actions.click_element(By.XPATH, '//button[@aria-label="Previous month" and @title="Previous month"]')

        # 「展開終了日」を選択
        if is_next_month:
            actions.click_element(By.XPATH, '//button[@aria-label="Next month" and @title="Next month"]')
            actions.click_element(By.XPATH, f'//button[@role="gridcell" and text()="{end_day}"]')

        if not is_next_month:
            actions.click_element(By.XPATH, f'//button[@role="gridcell" and text()="{end_day}"]')

        # 「展開終了日」/「時」の入力欄をクリック
        actions.click_element(By.XPATH, '(//input[@type="number" and @min="0" and @max="23" and @step="1"])[2]')

        # 「展開終了日」/「時」を入力
        driver.find_element(By.XPATH, '(//input[@type="number" and @min="0" and @max="23" and @step="1"])[2]').send_keys(str(current_hour))
        actions.current_step()

        # 「展開終了日」/「分」の入力欄をクリック
        actions.click_element(By.XPATH, '(//input[@type="number" and @min="0" and @max="59" and @step="1"])[2]')

        # 「展開終了日」/「分」を入力
        driver.find_element(By.XPATH, '(//input[@type="number" and @min="0" and @max="59" and @step="1"])[2]').send_keys(str(current_minute))
        actions.current_step()

        # 「MN日付」の「日付を選択」ボタンをクリック
        actions.click_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div[7]/div/div/div[1]/div/div/div/div/div/button')

        # 本週の月曜日の日付を選択
        if this_week_monday.month != datetime.now().month:
            actions.click_element(By.XPATH, '//button[@aria-label="Previous month" and @title="Previous month"]')
        monday_day = this_week_monday.day
        actions.click_element(By.XPATH, f'//button[@role="gridcell" and text()="{monday_day}"]')

        # 「施策名」を入力欄をクリック
        measure_name_element = driver.find_element(By.XPATH,
                                                   '//div[@class="sc-kYWVYA sc-eEOqmf fDeVho jzMarX MuiInputBase-root '
                                                   'MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth'
                                                   ' MuiInputBase-formControl"]/input[@type="text" and @class="sc-yeoIj '
                                                   'sc-lkwKjF kAIamR hpFbeN MuiInputBase-input MuiOutlinedInput-input"]')
        driver.execute_script("arguments[0].click();", measure_name_element)
        actions.current_step()

        # 「施策名」を入力
        driver.execute_script("arguments[0].value='12345';", measure_name_element)
        actions.current_step()

        # 「施策内容」を入力欄をクリック
        measures_details = driver.find_element(By.XPATH,
                                               '//div[@class="sc-kYWVYA sc-eEOqmf jYGbKl bhNThq MuiInputBase-root '
                                               'MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth '
                                               'MuiInputBase-formControl MuiInputBase-multiline"]/textarea[@rows="4" and '
                                               '@class="sc-yeoIj sc-lkwKjF dgeVju jdREmE MuiInputBase-input '
                                               'MuiOutlinedInput-input MuiInputBase-inputMultiline"]')
        driver.execute_script("arguments[0].click();", measures_details)
        actions.current_step()

        # 「施策内容」を入力
        driver.execute_script("arguments[0].value='12345';", measures_details)
        actions.current_step()

        actions.save_test_results()


    except NoSuchElementException as e:

        error_message = str(e).split("\n")[0]
        print(Fore.RED + f"テスト中に要素が見つかりませんでした: {error_message}")
        send_slack_message(f"❌ テスト中にエラーが発生しました: {error_message}")

    except Exception as e:
        error_message = str(e)
        print(Fore.RED + f"テスト中にエラーが発生しました: {error_message}")
        send_slack_message(f"❌ テスト中にエラーが発生しました: {error_message}")


def main():
    driver = None
    try:
        driver = initialize_browser()
        actions = SeleniumActions(driver, pd.read_excel('test_cases.xlsx'))
        send_slack_message("🛠 自動テストを開始します...")

        execute_test_case(driver, config['DEFAULT']['url'], config['DEFAULT']['email'], config['DEFAULT']['password'], actions)

    except Exception as e:
        print(Fore.RED + f"テスト中にエラーが発生しました: {str(e)}")
    finally:
        if driver:
            driver.quit()
            print(Fore.YELLOW + "ブラウザが正常に閉じられました。")



if __name__ == "__main__":
    main()
