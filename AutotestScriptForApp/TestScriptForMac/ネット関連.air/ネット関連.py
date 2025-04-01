# -*- encoding=utf8 -*-
__author__ = "joseishou"

from airtest.core.api import *
from airtest.report.report import simple_report

auto_setup(__file__, logdir=True, devices=["ios:///127.0.0.1:8100"])


def net_connect():
    touch(Template(r"tpl1703052395763.png", record_pos=(-0.462, 0.212), resolution=(2160, 1620)))  # コントローラーセンターを開く
    time.sleep(2)
    touch(Template(r"tpl1703052424656.png", record_pos=(0.102, 0.192), resolution=(2160, 1620)))  # コントローラーセンターを開く
    time.sleep(2)
    touch(Template(r"tpl1703053314808.png", record_pos=(0.222, -0.185), resolution=(2160, 1620)))  # Wi-Fi接続
    time.sleep(2)
    touch((0.500, 0.500))  # コントローラーセンターを閉じる
    time.sleep(2)


def net_disconnect():
    touch(Template(r"tpl1703052395763.png", record_pos=(-0.462, 0.212), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1703052424656.png", record_pos=(0.102, 0.192), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1703052449113.png", record_pos=(0.223, -0.184), resolution=(2160, 1620)))  # Wi-Fi接続を切る
    time.sleep(2)
    touch((0.500, 0.500))  # コントローラーセンターを閉じる
    time.sleep(2)


def login():
    touch(Template(r"tpl1703052395763.png", record_pos=(-0.462, 0.212), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1703052424656.png", record_pos=(0.102, 0.192), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1703053314808.png", record_pos=(0.222, -0.185), resolution=(2160, 1620)))  # Wi-Fi接続
    time.sleep(2)
    touch((0.500, 0.500))
    time.sleep(2)
    text("12qwaszx!", enter=False)  # パスワード入力
    time.sleep(2)
    touch(Template(r"tpl1684723341307.png", record_pos=(0.001, -0.106), resolution=(2160, 1620)))  # "OK"をタップ
    time.sleep(12)
    if exists(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620))):  # ダイアログ判断
        touch(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620)))  # 画面転移キャンセル
        time.sleep(3)


dev = device()
dev.start_recording(output="test.mp4", max_time="36000", orientation=2)
try:
    net_disconnect()

    start_app("jp.co.couger.ludens")  # アプリ起動
    time.sleep(3)

    net_connect()
    time.sleep(20)

    net_disconnect()

    text("12qwaszx!", enter=False)  #パスワード入力する
    time.sleep(2)

    touch(Template(r"tpl1684723341307.png", record_pos=(0.001, -0.106), resolution=(2160, 1620)))  # "OK"をタップ
    time.sleep(2)

    login()

    net_disconnect()
    touch(Template(r"tpl1703059824599.png", record_pos=(0.279, -0.232), resolution=(2160, 1620)))  # 前日のデータをタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1703059824599.png", record_pos=(0.279, -0.232), resolution=(2160, 1620)))  # 前日のデータをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1703062943715.png", record_pos=(0.433, -0.268), resolution=(2160, 1620)))  # Xをタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1703059824599.png", record_pos=(0.279, -0.232), resolution=(2160, 1620)))  # 前日のデータをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1703064956910.png", record_pos=(-0.009, 0.268), resolution=(2160, 1620)))  # 自分の記録をタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1703059824599.png", record_pos=(0.279, -0.232), resolution=(2160, 1620)))  # 前日のデータをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1703065134224.png", record_pos=(0.29, -0.268), resolution=(2160, 1620)))  # 前日をタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1703059824599.png", record_pos=(0.279, -0.232), resolution=(2160, 1620)))  # 前日のデータをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1703065711905.png", record_pos=(0.4, 0.269), resolution=(2160, 1620)))  # 廃棄予算設定をタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1703059824599.png", record_pos=(0.279, -0.232), resolution=(2160, 1620)))  # 前日のデータをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1703067187009.png", record_pos=(0.379, 0.206), resolution=(2160, 1620)))  # カテゴリーで見るをタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1703059824599.png", record_pos=(0.279, -0.232), resolution=(2160, 1620)))  # 前日のデータをタップ
    time.sleep(3)
    touch(Template(r"tpl1703065711905.png", record_pos=(0.4, 0.269), resolution=(2160, 1620)))  # 廃棄予算設定をタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1703133632944.png", record_pos=(0.064, 0.214), resolution=(2160, 1620)))  # キャンセルをタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1703059824599.png", record_pos=(0.279, -0.232), resolution=(2160, 1620)))  # 前日のデータをタップ
    time.sleep(3)
    touch(Template(r"tpl1703065711905.png", record_pos=(0.4, 0.269), resolution=(2160, 1620)))  # 廃棄予算設定をタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1703133982106.png", record_pos=(0.32, 0.215), resolution=(2160, 1620)))  # 設定するをタップ
    time.sleep(5)

    login()

    net_disconnect()
    touch(Template(r"tpl1703135563744.png", record_pos=(0.282, -0.161), resolution=(2160, 1620)))  # 発注ポイントをタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1703135563744.png", record_pos=(0.282, -0.161), resolution=(2160, 1620)))  # 発注ポイントをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1703062943715.png", record_pos=(0.433, -0.268), resolution=(2160, 1620)))  # Xをタップ

    login()

    net_disconnect()
    touch(Template(r"tpl1705049908597.png", record_pos=(0.271, -0.091), resolution=(2160, 1620)))  # やることリストをタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1705049908597.png", record_pos=(0.271, -0.091), resolution=(2160, 1620)))  # やることリストをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1705050253207.png", record_pos=(0.432, -0.281), resolution=(2160, 1620)))  # Xをタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1705049908597.png", record_pos=(0.271, -0.091), resolution=(2160, 1620)))  # やることリストをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1705285280866.png", record_pos=(-0.08, -0.275), resolution=(2160, 1620)))  # 事前発注をタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1705049908597.png", record_pos=(0.271, -0.091), resolution=(2160, 1620)))  # やることリストをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1705285485974.png", record_pos=(0.096, -0.274), resolution=(2160, 1620)))  # オペレーションをタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1705049908597.png", record_pos=(0.271, -0.091), resolution=(2160, 1620)))  # やることリストをタップ
    time.sleep(3)
    touch(Template(r"tpl1705285485974.png", record_pos=(0.096, -0.274), resolution=(2160, 1620)))  # オペレーションをタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1705287419422.png", record_pos=(0.315, -0.094), resolution=(2160, 1620)))
    time.sleep(5)

    login()

    touch(Template(r"tpl1705049908597.png", record_pos=(0.271, -0.091), resolution=(2160, 1620)))  # やることリストをタップ
    time.sleep(3)
    touch(Template(r"tpl1705285485974.png", record_pos=(0.096, -0.274), resolution=(2160, 1620)))  # オペレーションをタップ
    time.sleep(3)
    touch(Template(r"tpl1705293424926.png", record_pos=(0.394, 0.1), resolution=(2160, 1620)))  # 写真を送るをタップ
    time.sleep(3)
    touch(Template(r"tpl1705293809362.png", record_pos=(-0.001, 0.24), resolution=(2160, 1620)))  # 写真を選ぶをタップ
    time.sleep(3)
    touch(Template(r"tpl1705294343580.png", record_pos=(-0.229, 0.254), resolution=(2160, 1620)))  # 写真ライブラリをタップ
    time.sleep(3)
    touch((0.4, 0.301))  # 写真を選択
    time.sleep(3)
    touch(Template(r"tpl1705294498670.png", record_pos=(0.29, -0.333), resolution=(2160, 1620)))  # 完了をタップ
    time.sleep(3)

    net_disconnect()
    touch(Template(r"tpl1705297181188.png", record_pos=(-0.001, 0.305), resolution=(2160, 1620)))  # 写真を送信をタップ
    time.sleep(5)

    login()

    touch(Template(r"tpl1705049908597.png", record_pos=(0.271, -0.091), resolution=(2160, 1620)))  # やることリストをタップ
    time.sleep(3)
    touch(Template(r"tpl1705285485974.png", record_pos=(0.096, -0.274), resolution=(2160, 1620)))  # オペレーションをタップ
    time.sleep(3)
    touch(Template(r"tpl1705293424926.png", record_pos=(0.394, 0.1), resolution=(2160, 1620)))  # 写真を送るをタップ
    time.sleep(3)
    touch(Template(r"tpl1705293809362.png", record_pos=(-0.001, 0.24), resolution=(2160, 1620)))  # 写真を選ぶをタップ
    time.sleep(3)
    touch(Template(r"tpl1705294343580.png", record_pos=(-0.229, 0.254), resolution=(2160, 1620)))  # 写真ライブラリをタップ
    time.sleep(3)
    touch((0.4, 0.301))  # 写真を選択
    time.sleep(3)
    touch(Template(r"tpl1705294498670.png", record_pos=(0.29, -0.333), resolution=(2160, 1620)))  # 完了をタップ
    time.sleep(3)
    touch(Template(r"tpl1705297181188.png", record_pos=(-0.001, 0.305), resolution=(2160, 1620)))  # 写真を送信をタップ
    time.sleep(3)
finally:
    dev.stop_recording()
    simple_report(__file__, logpath=True)
