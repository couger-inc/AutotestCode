import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.implicitly_wait(20)
# "flux"webを開く
driver.get("https://flux.fmcl-dev.ludens.to/signIn")
# ブラウザーをmaxサイズに
driver.maximize_window()
# アカウントを入力
driver.find_element(By.ID, "email").send_keys("shengqing@couger.co.jp")
# パスワードを入力
driver.find_element(By.ID, "password").send_keys("1234eszxcv!")
# "OK"ボタンをクリック(ログイン)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/form/div[3]/button").click()


"""データ分析(やることリスト)"""


# データー分析をクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div/div[1]/ul/button[3]/h3").click()
time.sleep(1)
# やることリストをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[1]/h3").click()
time.sleep(1)
# "前の日のデータ"を表示
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/button").click()
time.sleep(1)
# 右ボタンをクリック(本日に戻る)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/button[2]").click()
time.sleep(1)
# "リフレッシュ"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[2]/button").click()
time.sleep(3)
# "!""X"のみ表示をキャンセル
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/span/input").click()
time.sleep(1)
# "!""X"のみ表示
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/span/input").click()
time.sleep(1)


"""店舗名フィルター"""



# "店舗名フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[1]/div/div[2]/button").click()
time.sleep(1)
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()


"""施策区分フィルター"""


# "施策区分フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
time.sleep(1)
# "すべて選択"をキャンセル
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# "取組みポイント"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[2]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)
# "施策区分フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
time.sleep(1)
# "取組みポイント"をキャンセル
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[2]/div/span/input").click()
time.sleep(1)
# "新商品"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[3]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)
# "施策区分フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
time.sleep(1)
# "新商品"をキャンセル
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[3]/div/span/input").click()
time.sleep(1)
# "今お得"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[4]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)
# "施策区分フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
time.sleep(1)
# "今お得"をキャンセル
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[4]/div/span/input").click()
time.sleep(1)
# "事前発注"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[5]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)
# "施策区分フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
time.sleep(1)
# "事前発注"をキャンセル
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[5]/div/span/input").click()
time.sleep(1)
# "1個もらえる企画"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[6]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)
# "施策区分フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
time.sleep(1)
# もう一度"すべて選択"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)


"""中分類フィルター"""


try:
    # "中分類フィルター"開く
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[3]/div/div[2]/button").click()
    time.sleep(1)
    # "すべて選択"をキャンセル
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
    time.sleep(1)
    # "すべて選択"を選択
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
    time.sleep(1)
    # "確定"ボタンをクリック
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
    time.sleep(1)
except NoSuchElementException:
    pass


"""10時以降フィルター"""


# "10時以降フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[9]/div/div[2]/button").click()
time.sleep(1)
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)


"""達成状況フィルター"""


# "達成状況フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[10]/div/div[2]/button").click()
time.sleep(1)
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# "未発注"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[2]/div/span/input").click()
time.sleep(1)
# "在庫要確認"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[3]/div/span/input").click()
time.sleep(1)
# "目標未達"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[4]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)


"""リージョンの選択"""


# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第１リージョン"を選択
driver.find_element(By.ID, ":r1:-option-1").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第２リージョン"を選択
driver.find_element(By.ID, ":r1:-option-2").click()
time.sleep(1)
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "杉並営業所"を選択
driver.find_element(By.ID, ":r3:-option-1").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第３リージョン"を選択
driver.find_element(By.ID, ":r1:-option-3").click()
time.sleep(1)
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "青梅営業所"を選択
driver.find_element(By.ID, ":r3:-option-1").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "ライン・法人室"を選択
driver.find_element(By.ID, ":r1:-option-4").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "埼玉リージョン"を選択
driver.find_element(By.ID, ":r1:-option-0").click()
time.sleep(1)


"""データ分析(やることリスト=>オペレーション)"""


# "オペレーション"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[1]/div/button[2]").click()
time.sleep(1)
# "!"のみ表示をキャンセル
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/span/input").click()
time.sleep(1)
# "!"のみ表示を選択
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/span/input").click()
time.sleep(1)


"""店舗名フィルター"""
# "店舗名フィルター"開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/button").click()
time.sleep(1)
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)
# "全て閉じる(タスク欄)"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[1]/div/div[1]/button").click()
time.sleep(1)
# "!"のみ表示をキャンセル
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/span/input").click()
time.sleep(1)
# "!"のみ表示を選択
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/span/input").click()
time.sleep(1)
# "全て開く(タスク欄)"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[1]/div/div[1]/button").click()
time.sleep(1)


"""実施日フィルター"""


# "実施日"フィルターを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
time.sleep(1)
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)


"""状況詳細フィルター"""


# "状況詳細"フィルターを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[4]/div/div[2]/button").click()
time.sleep(1)
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
time.sleep(1)
# "未完了"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[3]/div/span/input").click()
time.sleep(1)
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
time.sleep(1)


"""リージョン選択"""


# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第１リージョン"を選択
driver.find_element(By.ID, ":r1:-option-1").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第２リージョン"を選択
driver.find_element(By.ID, ":r1:-option-2").click()
time.sleep(1)
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "杉並営業所"を選択
driver.find_element(By.ID, ":r3:-option-1").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第３リージョン"を選択
driver.find_element(By.ID, ":r1:-option-3").click()
time.sleep(1)
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "青梅営業所"を選択
driver.find_element(By.ID, ":r3:-option-1").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "ライン・法人室"を選択
driver.find_element(By.ID, ":r1:-option-4").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "埼玉リージョン"を選択
driver.find_element(By.ID, ":r1:-option-0").click()


"""データ分析(ダッシュボード)"""


# データー分析をクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div/div[1]/ul/button[3]/h3").click()
time.sleep(1)
# "ダッシュボード"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]").click()
time.sleep(1)


"""施策導入状況"""


# "施策導入状況"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/button[2]").click()
time.sleep(1)
# "左ボタン(前週のデータ)"をクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/button").click()
time.sleep(1)
# "右ボタン"をクリック(本週に戻る)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[3]/button").click()
time.sleep(1)
# "新商品"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/button[2]").click()
time.sleep(1)
# "今お得"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/button[3]").click()
time.sleep(1)
# "事前発注"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/button[4]").click()
time.sleep(1)


"""月間販売実績"""


# "月間販売実績"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/button[3]").click()
time.sleep(1)
"""米飯"""
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[3]/button").click()
time.sleep(1)
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "寿司"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "チルド寿司"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "弁当"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "チルド弁当"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]").click()
time.sleep(1)
"""調理麺"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
time.sleep(1)
# "調理麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]").click()
time.sleep(1)
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "温かい麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "パスタ"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "焼麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
"""調理パン"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
time.sleep(1)
# "調理パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[3]").click()
time.sleep(1)
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "バラエティーロール"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "ハンバーガー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "ＬＬ調理パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
"""サラダ"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
time.sleep(1)
# "サラダ"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[4]").click()
time.sleep(1)
# "サラダの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "サラダドレッシング"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
"""惣菜"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
time.sleep(1)
# "惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[5]").click()
time.sleep(1)
# "惣菜の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "パウチ惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "惣菜の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "スープ・軽食"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
"""デザート"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
time.sleep(1)
# "デザート"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[6]").click()
time.sleep(1)
# "デザートの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "ＮＢデザート"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "デザートの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "ヨーグルト"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
"""カウンターFF"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
time.sleep(1)
# "カウンターFF"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[7]").click()
time.sleep(1)
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "中華まん・スチーマー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "フライヤー・常温惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "カウンターコーヒー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
"""パン"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
time.sleep(1)
# "パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[8]").click()
time.sleep(1)
# "パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "菓子パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "惣菜パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)


"""品揃え"""


# "品揃え"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/button[4]").click()
time.sleep(1)
"""米飯"""
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "寿司"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "チルド寿司"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "弁当"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "チルド弁当"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)

"""調理麺"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
time.sleep(1)
# "調理麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "温かい麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "パスタ"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "焼麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)

"""調理パン"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
time.sleep(1)
# "調理パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[3]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "バラエティーロール"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "ハンバーガー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "ＬＬ調理パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)

"""サラダ"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
time.sleep(1)
# "サラダ"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[4]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "サラダの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "サラダドレッシング"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)

"""惣菜"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
time.sleep(1)
# "惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[5]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "惣菜の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "パウチ惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "惣菜の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "スープ・軽食"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)

"""デザート"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
time.sleep(1)
# "デザート"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[6]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "デザートの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "ＮＢデザート"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "デザートの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "ヨーグルト"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)

"""カウンターFF"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
time.sleep(1)
# "カウンターFF"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[7]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "中華まん・スチーマー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "フライヤー・常温惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "カウンターコーヒー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)

"""パン"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
time.sleep(1)
# "パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[8]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "菓子パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)
# "パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "惣菜パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
time.sleep(1)
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
time.sleep(1)
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
time.sleep(1)
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(1)



"""店舗の記録"""
# "店舗の記録"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/button[5]").click()
time.sleep(1)


"""リージョンと店舗の選択"""
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第１リージョン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
time.sleep(1)
# "メトロ外苑前"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
time.sleep(1)
# "王子駅南口"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
time.sleep(1)
# "杉並宮前二丁目"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
time.sleep(1)
# "としまエコミューゼタウン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
time.sleep(1)
# "太子堂"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[6]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第２リージョン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "杉並営業所"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "東京第３リージョン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/div/button").click()
time.sleep(1)
# "青梅営業所"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
time.sleep(1)
# "福生駅前"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
time.sleep(1)
# "青梅新町四丁目"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/div/button").click()
time.sleep(1)
# "ライン・法人室"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]").click()
time.sleep(1)
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
time.sleep(1)