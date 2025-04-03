import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from colorama import init, Fore
from datetime import datetime
import configparser
from selenium.webdriver.common.keys import Keys

# 現在の日付を取得し、YYYYMMDD としてフォーマット
current_date = datetime.now().strftime("%Y/%m/%d")

# coloramaを初期化
init(autoreset=True)

# 設定ファイルを読み込む
config = configparser.ConfigParser()
config.read('config.ini')

# テストケースのExcelファイルを読み込む
global_test_cases_df = pd.read_excel('test_cases.xlsx')

# テスト結果リストを初期化
global_test_log = []


class SeleniumActions:
    def __init__(self, driver, test_cases_df):
        self.driver = driver
        self.local_test_cases_df = test_cases_df
        self.test_log = []
        self.step_counter = 1
        self.original_window = driver.current_window_handle

    def current_step(self, color=Fore.LIGHTGREEN_EX):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = "成功"

        try:
            step_description = self.local_test_cases_df.loc[self.local_test_cases_df['No'] == self.step_counter, 'case'].values[0]
            if pd.isna(step_description) or step_description == '':
                raise ValueError("case説明が空です。")
        except IndexError:
            step_description = "case説明が見つかりません。"
            color = Fore.RED
            result = "失敗"
        except ValueError as ve:
            step_description = str(ve)
            color = Fore.RED
            result = "失敗"

        step_description = str(step_description)
        print(f"{self.step_counter}: " + Fore.YELLOW + f"[{current_time}] " + color + step_description)

        self.test_log.append({
            "No": self.step_counter,
            "Time": current_time,
            "Description": step_description,
            "Result": result
        })

        self.step_counter += 1

    def enter_text(self, by, identifier, text):
        element = self.driver.find_element(by, identifier)
        element.send_keys(text)

    def select_and_delete_text(self, by, identifier):
        element = self.driver.find_element(by, identifier)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

    def click_element(self, by, identifier):
        element = self.driver.find_element(by, identifier)
        element.click()

    def double_click_element(self, by, identifier):
        element = self.driver.find_element(by, identifier)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def move_to_element(self, by, identifier):
        element = self.driver.find_element(by, identifier)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def press_key(self, by, identifier, key):
        element = self.driver.find_element(by, identifier)
        element.send_keys(key)

    def switch_to_original_tab(self):
        self.driver.switch_to.window(self.original_window)

    def save_test_results(self):
        test_log_df = pd.DataFrame(self.test_log)
        test_log_df.to_excel('test_log.xlsx', index=False)
        print(Fore.LIGHTMAGENTA_EX + "テスト結果が保存されました。")

        html_report = test_log_df.to_html()
        with open('test_log.html', 'w') as f:
            f.write(html_report)
        print(Fore.LIGHTGREEN_EX + "HTMLテストレポートが生成されました。")


def initialize_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    return driver


def custom_print(message, color=Fore.LIGHTGREEN_EX):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] " + color + message)


def execute_test_case(driver, url, email, password, actions):
    driver.get(url)
    actions.current_step()

    driver.maximize_window()
    actions.current_step()

    actions.enter_text(By.ID, "email", email)
    actions.enter_text(By.ID, "password", password)
    actions.click_element(By.XPATH, "//button[contains(text(), 'ログイン')]")
    time.sleep(5)

    for times in range(100000):
        custom_print(f"Executing loop iteration {times + 1}: Entering '入力した内容を削除欄をクリックして、「チケットの払い戻し方法を教えて」を入力する'")
        actions.enter_text(By.ID, "input-with-icon-textfield", "チケットの払い戻し方法を教えて")
        custom_print(f"Executing loop iteration {times + 1}: Entering '検索する'")
        actions.press_key(By.ID, "input-with-icon-textfield", Keys.RETURN)

        custom_print(f"Executing loop iteration {times + 1}: 入力した内容を削除")
        actions.select_and_delete_text(By.ID, "input-with-icon-textfield")

        custom_print(f"Executing loop iteration {times + 1}: Entering '入力した内容を削除欄をクリックして、「雑誌の返品方法を教えて」を入力する'")
        actions.enter_text(By.ID, "input-with-icon-textfield", "雑誌の返品方法を教えて")
        custom_print(f"Executing loop iteration {times + 1}: Entering '検索する'")
        actions.press_key(By.ID, "input-with-icon-textfield", Keys.RETURN)

        custom_print(f"Executing loop iteration {times + 1}: 入力した内容を削除")
        actions.select_and_delete_text(By.ID, "input-with-icon-textfield")


def main():
    driver = initialize_browser()
    actions = SeleniumActions(driver, global_test_cases_df)
    actions.current_step()
    execute_test_case(driver, config['DEFAULT']['url'], config['DEFAULT']['email'], config['DEFAULT']['password'], actions)
    input("ブラウザを閉じるにはEnterキーを押してください...")
    actions.save_test_results()
    driver.quit()


if __name__ == "__main__":
    main()
