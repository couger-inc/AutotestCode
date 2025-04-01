# -*- encoding=utf8 -*-
__author__ = "shengqing"

from airtest.core.api import *

auto_setup(__file__)

# -*- encoding=utf8 -*-
__author__ = "shengqing"

from airtest.core.api import *

auto_setup(__file__)

id_list=["2_4_3000-1_A","2_4_3001-1_A","2_4_3002-1_A","2_4_3003-1_A","2_4_3100-1_A","2_4_3101-1_A","2_4_3200-1_A","2_4_3201-1_A","2_4_3202-1_A","2_4_3203-1_A","2_4_3204-1_A","2_4_3205-1_A","2_4_3206-1_A","2_4_3300-1_A","2_4_3301-1_A","2_4_3302-1_A","2_4_3303-1_A","2_4_3300-2_A","2_4_3301-2_A","2_4_3302-2_A","2_4_3304-2_A","2_4_3300-3_A","2_4_3301-3_A","2_4_3303-3_A","2_4_3305-3_A","2_4_3300-4_A","2_4_3301-4_A","2_4_3304-4_A","2_4_3305-4_A","2_4_3306-5_A","2_4_3301-5_A","2_4_3302-5_A","2_4_3303-5_A","2_4_3306-6_A","2_4_3301-6_A","2_4_3302-6_A","2_4_3304-6_A","2_4_3306-7_A","2_4_3301-7_A","2_4_3303-7_A","2_4_3305-7_A","2_4_3306-8_A","2_4_3301-8_A","2_4_3304-8_A","2_4_3305-8_A","2_4_3307-9_A","2_4_3301-9_A","2_4_3302-9_A","2_4_3303-9_A","2_4_3307-10_A","2_4_3301-10_A","2_4_3302-10_A","2_4_3304-10_A","2_4_3307-11_A","2_4_3301-11_A","2_4_3303-11_A","2_4_3305-11_A","2_4_3307-12_A","2_4_3301-12_A","2_4_3304-12_A","2_4_3305-12_A","2_4_3308-13_A","2_4_3301-13_A","2_4_3302-13_A","2_4_3303-13_A","2_4_3308-14_A","2_4_3301-14_A","2_4_3302-14_A","2_4_3304-14_A","2_4_3308-15_A","2_4_3301-15_A","2_4_3303-15_A","2_4_3305-15_A","2_4_3308-16_A","2_4_3301-16_A","2_4_3304-16_A","2_4_3305-16_A","2_4_3309-17_A","2_4_3301-17_A","2_4_3302-17_A","2_4_3303-17_A","2_4_3310-18_A","2_4_3301-18_A","2_4_3302-18_A","2_4_3304-18_A","2_4_3311-19_A","2_4_3301-19_A","2_4_3303-19_A","2_4_3305-19_A","2_4_3312-20_A","2_4_3301-20_A","2_4_3304-20_A","2_4_3305-20_A","2_4_3313-21_A","2_4_3301-21_A","2_4_3302-21_A","2_4_3303-21_A","2_4_3314-22_A","2_4_3301-22_A","2_4_3302-22_A","2_4_3304-22_A","2_4_3315-23_A","2_4_3301-23_A","2_4_3303-23_A","2_4_3305-23_A","2_4_3316-24_A","2_4_3301-24_A","2_4_3304-24_A","2_4_3305-24_A","2_4_3317-25_A","2_4_3301-25_A","2_4_3302-25_A","2_4_3303-25_A","2_4_3318-26_A","2_4_3301-26_A","2_4_3302-26_A","2_4_3304-26_A","2_4_3319-27_A","2_4_3301-27_A","2_4_3303-27_A","2_4_3305-27_A","2_4_3320-28_A","2_4_3301-28_A","2_4_3304-28_A","2_4_3305-28_A"]


times = 42
while times< 125:
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
    touch(Template(r"tpl1688094367415.png", record_pos=(-0.26, -0.092), resolution=(2160, 1620)))  # 編集したい画面名を選択
    sleep(2)
    touch(Template(r"tpl1693297723263.png", record_pos=(-0.312, -0.045), resolution=(2160, 1620)))  # 編集したい画面名を選択
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
    touch(Template(r"tpl1693297778697.png", record_pos=(0.303, -0.162), resolution=(2160, 1620)))   # 前週のレビューをタップ
    sleep(2)
    touch(Template(r"tpl1688102693380.png", record_pos=(0.462, 0.302), resolution=(2160, 1620)))    # 録画操作開始
    sleep(2)
    touch(Template(r"tpl1688102879994.png", record_pos=(0.105, 0.192), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688102908450.png", record_pos=(0.297, 0.175), resolution=(2160, 1620)))    # 録画開始
    sleep(1)
    touch((407,832))
    sleep(2)
    touch(Template(r"tpl1693297808147.png", record_pos=(0.053, -0.274), resolution=(2160, 1620)))   # 日々の変化をタップ
    sleep(15)
    touch(Template(r"tpl1688103018677.png", record_pos=(0.462, 0.302), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688102879994.png", record_pos=(0.105, 0.192), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688103063774.png", record_pos=(0.298, 0.176), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1688606790510.png", record_pos=(-0.276, 0.135), resolution=(2160, 1620)))   # 録画終わる
    sleep(2)
    touch((36,1579))    # デバッグ画面開く（ログのペースト）
    sleep(2)
    touch(Template(r"tpl1688106585731.png", record_pos=(-0.301, 0.254), resolution=(2160, 1620)))
    sleep(2)
    touch(Template(r"tpl1693297903003.png", record_pos=(-0.298, -0.181), resolution=(2160, 1620)))
    sleep(2)
    stop_app("jp.co.couger.ludens")
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
    stop_app("com.google.Docs")  # ドキュメントを閉じる
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
    stop_app("com.apple.mobileslideshow")
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