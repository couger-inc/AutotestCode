
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

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
# やることリストをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[1]/h3").click()
# "前の日のデータ"を表示
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/button").click()
# 右ボタンをクリック(本日に戻る)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/button[2]").click()
# "リフレッシュ"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[2]/button").click()
# "!""X"のみ表示をキャンセル
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/span/input").click()
# "!""X"のみ表示
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/span/input").click()
# "店舗名フィルター"展開
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[1]/div/div[2]/button").click()
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()


"""施策区分フィルター"""


# "施策区分フィルター"展開
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
# "すべて選択"をキャンセル
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# もう一度"すべて選択"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()


"""中分類フィルター"""


try:
    # "中分類フィルター"展開
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[3]/div/div[2]/button").click()

    # "すべて選択"をキャンセル
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()

    # "すべて選択"を選択
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()

    # "確定"ボタンをクリック
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()

except NoSuchElementException:
    pass


"""10時以降フィルター"""


# "10時以降フィルター"展開
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[9]/div/div[2]/button").click()
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()


"""達成状況フィルター"""


# "達成状況フィルター"展開
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[10]/div/div[2]/button").click()
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# "未発注"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[2]/div/span/input").click()
# "在庫要確認"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[3]/div/span/input").click()
# "目標未達"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[4]/div/span/input").click()
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()


"""リージョンの選択"""


# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "東京第１リージョン"を選択
driver.find_element(By.ID, ":r1:-option-1").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "東京第２リージョン"を選択
driver.find_element(By.ID, ":r1:-option-2").click()
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/button").click()
# "杉並営業所"を選択
driver.find_element(By.ID, ":r3:-option-1").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "東京第３リージョン"を選択
driver.find_element(By.ID, ":r1:-option-3").click()
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/button").click()
# "青梅営業所"を選択
driver.find_element(By.ID, ":r3:-option-1").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "ライン・法人室"を選択
driver.find_element(By.ID, ":r1:-option-4").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "埼玉リージョン"を選択
driver.find_element(By.ID, ":r1:-option-0").click()

time.sleep(3)
"""データ分析(やることリスト=>オペレーション)"""


# "オペレーション"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[1]/div/button[2]").click()
# "!"のみ表示をキャンセル
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/span/input").click()
# "!"のみ表示を選択
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/span/input").click()
# "店舗名フィルター"展開
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/button").click()
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()
# "全て閉じる(タスク欄)"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[1]/div/div[1]/button").click()
# "!"のみ表示をキャンセル
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/span/input").click()
# "!"のみ表示を選択
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/span/input").click()
# "全て開く(タスク欄)"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[1]/div/div[1]/button").click()


"""実施日フィルター"""


# "実施日"フィルターを展開
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[2]/div/div[2]/button").click()
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()


"""状況詳細フィルター"""


# "状況詳細"フィルターを展開
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[4]/div/div[2]/button").click()
# "すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# もう一度"すべて選択"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[1]/div/span/input").click()
# "未完了"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[1]/label[3]/div/span/input").click()
# "確定"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/div[2]/button").click()


"""リージョン選択"""


# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "東京第１リージョン"を選択
driver.find_element(By.ID, ":r1:-option-1").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "東京第２リージョン"を選択
driver.find_element(By.ID, ":r1:-option-2").click()
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/button").click()
# "杉並営業所"を選択
driver.find_element(By.ID, ":r3:-option-1").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "東京第３リージョン"を選択
driver.find_element(By.ID, ":r1:-option-3").click()
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/button").click()
# "青梅営業所"を選択
driver.find_element(By.ID, ":r3:-option-1").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "ライン・法人室"を選択
driver.find_element(By.ID, ":r1:-option-4").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/button").click()
# "埼玉リージョン"を選択
driver.find_element(By.ID, ":r1:-option-0").click()


"""データ分析(ダッシュボード)"""


# データー分析をクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div/div[1]/ul/button[3]/h3").click()
# "ダッシュボード"をクリック
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]").click()


"""施策導入状況"""


# "施策導入状況"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/button[2]").click()
# "左ボタン(前週のデータ)"をクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/button").click()
# "右ボタン"をクリック(本週に戻る)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[3]/button").click()
# "新商品"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/button[2]").click()
# "今お得"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/button[3]").click()
# "事前発注"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/button[4]").click()


"""月間販売実績"""


# "月間販売実績"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/button[3]").click()
"""米飯"""
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[3]/button").click()
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "寿司"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "チルド寿司"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "弁当"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "チルド弁当"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]").click()
"""調理麺"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
# "調理麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]").click()
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "温かい麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "パスタ"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "焼麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
"""調理パン"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
# "調理パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[3]").click()
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "バラエティーロール"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "ハンバーガー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "ＬＬ調理パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
"""サラダ"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
# "サラダ"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[4]").click()
# "サラダの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "サラダドレッシング"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
"""惣菜"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
# "惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[5]").click()
# "惣菜の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "パウチ惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "惣菜の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "スープ・軽食"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
"""デザート"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
# "デザート"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[6]").click()
# "デザートの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "ＮＢデザート"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "デザートの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "ヨーグルト"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
"""カウンターFF"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
# "カウンターFF"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[7]").click()
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "中華まん・スチーマー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "フライヤー・常温惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "カウンターコーヒー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
"""パン"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div").click()
# "パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[8]").click()
# "パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "菓子パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/button").click()
# "惣菜パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()


"""品揃え"""


# "品揃え"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/button[4]").click()
"""米飯"""
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "寿司"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "チルド寿司"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "弁当"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "米飯の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "チルド弁当"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()

"""調理麺"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
# "調理麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "温かい麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "パスタ"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "調理麺の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "焼麺"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()

"""調理パン"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
# "調理パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[3]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "バラエティーロール"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "ハンバーガー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "調理パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "ＬＬ調理パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()

"""サラダ"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
# "サラダ"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[4]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "サラダの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "サラダドレッシング"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()

"""惣菜"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
# "惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[5]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "惣菜の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "パウチ惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "惣菜の中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "スープ・軽食"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()

"""デザート"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
# "デザート"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[6]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "デザートの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "ＮＢデザート"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "デザートの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "ヨーグルト"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()

"""カウンターFF"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
# "カウンターFF"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[7]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "中華まん・スチーマー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "フライヤー・常温惣菜"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "カウンターFFの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "カウンターコーヒー"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()

"""パン"""
# "大分類"のプルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div").click()
# "パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[8]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "菓子パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()
# "パンの中分類"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/button").click()
# "惣菜パン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "金額"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[2]").click()
# "個数"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span[2]/div/button[1]").click()
# "前の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button").click()
# "次の週"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button").click()



"""店舗の記録"""
# "店舗の記録"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/button[5]").click()


"""リージョンと店舗の選択"""
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/div/button").click()
# "東京第１リージョン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
# "メトロ外苑前"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
# "王子駅南口"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
# "杉並宮前二丁目"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
# "としまエコミューゼタウン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
# "太子堂"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[6]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/div/button").click()
# "東京第２リージョン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/div/button").click()
# "杉並営業所"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/div/button").click()
# "東京第３リージョン"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "営業所"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/div/button").click()
# "青梅営業所"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
# "福生駅前"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "店舗"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div/div/button").click()
# "青梅新町四丁目"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[3]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()
# "リージョン"プルダウンメニューを開く
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/div/button").click()
# "ライン・法人室"を選択
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]").click()
# "検索"ボタンをクリック
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/div[4]/button").click()