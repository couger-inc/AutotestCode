# -*- encoding=utf8 -*-
__author__ = "shengqing"

from airtest.core.api import *

auto_setup(__file__)
start_app("jp.co.couger.ludens")     #　アプリ起動
sleep(8)
text("12qwaszx!",enter = False)     #　アカウント入力
sleep(2)
touch(Template(r"tpl1688093014929.png", record_pos=(0.0, -0.107), resolution=(2160, 1620)))     # ログイン確認
sleep(15)
if exists(Template(r"tpl1688520868126.png", record_pos=(-0.107, 0.262), resolution=(2160, 1620))):
    touch(Template(r"tpl1688520868126.png", record_pos=(-0.107, 0.262), resolution=(2160, 1620)))   # 画面遷移キャンセル
    sleep(2)
touch((36,1579))    # デバッグ画面開く
sleep(2)
touch(Template(r"tpl1689058916693.png", record_pos=(-0.362, -0.091), resolution=(2160, 1620)))  # 編集したい画面名を選択
sleep(2)
swipe(Template(r"tpl1689158055015.png", record_pos=(-0.341, -0.03), resolution=(2160, 1620)), vector=[-0.0657, -0.1097])
sleep(2)
touch(Template(r"tpl1689058799662.png", record_pos=(-0.275, -0.05), resolution=(2160, 1620)))   # 編集したい画面名を選択
sleep(2)
touch(Template(r"tpl1688093979426.png", record_pos=(0.045, -0.093), resolution=(2160, 1620)))# id編集
sleep(2)
for t1 in range(5):
    text("\b",enter = False)    # empty　消去
sleep(2)
text("1_22_1")      #　id入力
sleep(2)
touch((36,1579))    # デバッグ画面閉じる
sleep(2)
touch(Template(r"tpl1688102693380.png", record_pos=(0.462, 0.302), resolution=(2160, 1620)))    # 録画操作開始
sleep(2)
touch(Template(r"tpl1688102879994.png", record_pos=(0.105, 0.192), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1688102908450.png", record_pos=(0.297, 0.175), resolution=(2160, 1620)))    # 録画開始
sleep(1)
touch((407,832))
sleep(2)
touch(Template(r"tpl1688095242918.png", record_pos=(0.305, 0.097), resolution=(2160, 1620)))   # 前週のレビューをタップ
sleep(5)
touch(Template(r"tpl1689058226512.png", record_pos=(0.346, -0.217), resolution=(2160, 1620)))
sleep(50)
touch(Template(r"tpl1688103018677.png", record_pos=(0.462, 0.302), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1688102879994.png", record_pos=(0.105, 0.192), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1688103063774.png", record_pos=(0.298, 0.176), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1689061244304.png", record_pos=(-0.289, -0.243), resolution=(2160, 1620)))  # 録画終わる
sleep(2)
touch((36,1579))    # デバッグ画面開く（ログのペースト）
sleep(2)
touch(Template(r"tpl1688106585731.png", record_pos=(-0.301, 0.254), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1689153223226.png", record_pos=(-0.287, -0.278), resolution=(2160, 1620)))
sleep(2)
stop_app("jp.co.couger.ludens")
sleep(2)
touch(Template(r"tpl1688377745654.png", record_pos=(0.257, 0.317), resolution=(2160, 1620)))    # ドライブを開く
sleep(2)
touch(Template(r"tpl1688435643613.png", record_pos=(0.45, 0.324), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1688377823676.png", record_pos=(0.246, 0.205), resolution=(2160, 1620)))
sleep(5)
text("1_22_1",enter=False)
sleep(2)
touch(Template(r"tpl1688434029766.png", record_pos=(0.081, -0.103), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1688371067702.png", record_pos=(-0.383, 0.022), resolution=(2160, 1620)))   # ログのペースト終わる
sleep(2)
touch(Template(r"tpl1688436713011.png", record_pos=(-0.474, -0.331), resolution=(2160, 1620)))
sleep(2)
stop_app("com.google.Docs")
sleep(2)
start_app("com.apple.mobileslideshow")   # 写真を開く
sleep(2)
touch((247,416),duration=2) # 動画を選択
sleep(2)
touch(Template(r"tpl1688523558148.png", record_pos=(-0.032, -0.274), resolution=(2160, 1620)))   # 動画を共有
sleep(2)
touch(Template(r"tpl1688523649995.png", record_pos=(-0.155, 0.251), resolution=(2160, 1620)))   # ファイルに保存を選択
sleep(2)
touch(Template(r"tpl1688523860826.png", record_pos=(-0.044, 0.265), resolution=(2160, 1620)))   # 動画名変更
sleep(2)
text("1_22_1")
sleep(2)
touch(Template(r"tpl1688523987229.png", record_pos=(0.343, -0.271), resolution=(2160, 1620)))   # 動画を保存
sleep(2)
touch((247,416),duration=2) # 動画を選択
sleep(2)
touch(Template(r"tpl1688524102332.png", record_pos=(-0.031, -0.071), resolution=(2160, 1620)))  # 動画を選択
sleep(2)
touch(Template(r"tpl1688524486273.png", record_pos=(-0.144, -0.175), resolution=(2160, 1620)))  # 動画を選削除
sleep(2)
stop_app("com.apple.mobileslideshow") # 写真アプリを閉じる
sleep(2)
touch(Template(r"tpl1688377745654.png", record_pos=(0.257, 0.317), resolution=(2160, 1620)))    # ドライブを開く
sleep(2)
touch(Template(r"tpl1688435643613.png", record_pos=(0.45, 0.324), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1688628728515.png", record_pos=(0.342, 0.093), resolution=(2160, 1620)))
sleep(2)
touch(Template(r"tpl1688628746131.png", record_pos=(-0.409, 0.346), resolution=(2160, 1620)))
sleep(2)
touch((920,423))
sleep(2)
start_app("com.apple.DocumentsApp")    # ファイルアプリ開く
sleep(2)
touch((837,290),duration=2)
sleep(2)
touch(Template(r"tpl1688629070582.png", record_pos=(-0.041, 0.292), resolution=(2160, 1620)))
sleep(2)
stop_app("com.apple.DocumentsApp")  # ファイルアプリを閉じる
sleep(3)
 
    
id_list=["2_22_1-1_A","2_22_10-1_A","2_22_11-1_A","2_22_12-1_A","2_22_13-1_A","2_22_14-1_A","2_22_15-1_A","2_22_16-1_A","2_22_17-1_A","2_22_1-1_E","2_22_10-1_E","2_22_11-1_E","2_22_12-1_E","2_22_13-1_E","2_22_14-1_E","2_22_15-1_E","2_22_16-1_E","2_22_17-1_E","2_22_1-1_K","2_22_10-1_K","2_22_11-1_K","2_22_12-1_K","2_22_13-1_K","2_22_14-1_K","2_22_15-1_K","2_22_16-1_K","2_22_17-1_K","2_22_1-1_S","2_22_10-1_S","2_22_11-1_S","2_22_12-1_S","2_22_13-1_S","2_22_14-1_S","2_22_15-1_S","2_22_16-1_S","2_22_17-1_S","9_22_1"]

times = 1
while times<37:
    start_app("jp.co.couger.ludens")     #　アプリ起動
    sleep(10)
    text("12qwaszx!",enter = False)     #　アカウント入力
    sleep(2)
    touch(Template(r"tpl1688093014929.png", record_pos=(0.0, -0.107), resolution=(2160, 1620)))     # ログイン確認
    sleep(15)
    if exists(Template(r"tpl1688520868126.png", record_pos=(-0.107, 0.262), resolution=(2160, 1620))):
        touch(Template(r"tpl1688520868126.png", record_pos=(-0.107, 0.262), resolution=(2160, 1620)))   # 画面遷移キャンセル
        sleep(2)
    touch((36,1579))    # デバッグ画面開く
    sleep(2)
    touch(Template(r"tpl1689058916693.png", record_pos=(-0.362, -0.091), resolution=(2160, 1620)))  # 編集したい画面名を選択
    sleep(2)
    swipe(Template(r"tpl1689158055015.png", record_pos=(-0.341, -0.03), resolution=(2160, 1620)), vector=[-0.0657, -0.1097])
    sleep(2)
    touch(Template(r"tpl1689058799662.png", record_pos=(-0.275, -0.05), resolution=(2160, 1620)))   # 編集したい画面名を選択
    sleep(2)
    touch(Template(r"tpl1688093979426.png", record_pos=(0.045, -0.093), resolution=(2160, 1620)))# id編集
    sleep(2)
    for t1 in range(5):
        text("\b",enter = False)    # empty　消去
    sleep(2)
    text(id_list[times])      #　id入力
    sleep(2)
    touch((36,1579))    # デバッグ画面閉じる
    sleep(2)
    touch(Template(r"tpl1688102693380.png", record_pos=(0.462, 0.302), resolution=(2160, 1620)))    # 録画操作開始
    sleep(2)
    touch(Template(r"tpl1688102879994.png", record_pos=(0.105, 0.192), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688102908450.png", record_pos=(0.297, 0.175), resolution=(2160, 1620)))    # 録画開始
    sleep(1)
    touch((407,832))
    sleep(2)
    touch(Template(r"tpl1688095242918.png", record_pos=(0.305, 0.097), resolution=(2160, 1620)))   # 前週のレビューをタップ
    sleep(5)
    touch(Template(r"tpl1689058226512.png", record_pos=(0.346, -0.217), resolution=(2160, 1620)))
    sleep(15)
    touch(Template(r"tpl1688103018677.png", record_pos=(0.462, 0.302), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688102879994.png", record_pos=(0.105, 0.192), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688103063774.png", record_pos=(0.298, 0.176), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1689061244304.png", record_pos=(-0.289, -0.243), resolution=(2160, 1620)))  # 録画終わる
    sleep(2)
    touch((36,1579))    # デバッグ画面開く（ログのペースト）
    sleep(2)
    touch(Template(r"tpl1688106585731.png", record_pos=(-0.301, 0.254), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1689153223226.png", record_pos=(-0.287, -0.278), resolution=(2160, 1620)))
    sleep(2)
    stop_app("jp.co.couger.ludens") #　アプリ閉じる
    sleep(2)
    touch(Template(r"tpl1688377745654.png", record_pos=(0.257, 0.317), resolution=(2160, 1620)))    # ドライブを開く
    sleep(2)
    touch(Template(r"tpl1688435643613.png", record_pos=(0.45, 0.324), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688377823676.png", record_pos=(0.246, 0.205), resolution=(2160, 1620)))
    sleep(5)
    text(id_list[times],enter=False)
    sleep(2)
    touch(Template(r"tpl1688434029766.png", record_pos=(0.081, -0.103), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688371067702.png", record_pos=(-0.383, 0.022), resolution=(2160, 1620)))   # ログのペースト終わる
    sleep(2)
    touch(Template(r"tpl1688436713011.png", record_pos=(-0.474, -0.331), resolution=(2160, 1620)))
    sleep(2)
    stop_app("com.google.Docs") # ドキュメントを閉じる
    sleep(2)
    start_app("com.apple.mobileslideshow")   # 写真を開く
    sleep(2)
    touch((247,416),duration=2) # 動画を選択
    sleep(2)
    touch(Template(r"tpl1688523558148.png", record_pos=(-0.032, -0.274), resolution=(2160, 1620)))   # 動画を共有
    sleep(2)
    touch(Template(r"tpl1688523649995.png", record_pos=(-0.155, 0.251), resolution=(2160, 1620)))   # ファイルに保存を選択
    sleep(2)
    touch(Template(r"tpl1688523860826.png", record_pos=(-0.044, 0.265), resolution=(2160, 1620)))   # 動画名変更
    sleep(2)
    text(id_list[times])
    sleep(2)
    touch(Template(r"tpl1688523987229.png", record_pos=(0.343, -0.271), resolution=(2160, 1620)))   # 動画を保存
    sleep(2)
    touch((247,416),duration=2) # 動画を選択
    sleep(2)
    touch(Template(r"tpl1688524102332.png", record_pos=(-0.031, -0.071), resolution=(2160, 1620)))  # 動画を選択
    sleep(2)
    touch(Template(r"tpl1688524486273.png", record_pos=(-0.144, -0.175), resolution=(2160, 1620)))  # 動画を選削除
    sleep(2)
    stop_app("com.apple.mobileslideshow") # 写真アプリを閉じる
    sleep(2)
    touch(Template(r"tpl1688377745654.png", record_pos=(0.257, 0.317), resolution=(2160, 1620)))    # ドライブを開く
    sleep(2)
    touch(Template(r"tpl1688435643613.png", record_pos=(0.45, 0.324), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688628728515.png", record_pos=(0.342, 0.093), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688628746131.png", record_pos=(-0.409, 0.346), resolution=(2160, 1620)))
    sleep(2)
    touch((920,423))
    sleep(2)
    start_app("com.apple.DocumentsApp")    # ファイルアプリ開く
    sleep(2)
    touch((837,290),duration=2)
    sleep(2)
    touch(Template(r"tpl1688629070582.png", record_pos=(-0.041, 0.292), resolution=(2160, 1620)))
    sleep(2)
    stop_app("com.apple.DocumentsApp") # ファイルアプリを閉じる
    sleep(3)
    times+=1
pass