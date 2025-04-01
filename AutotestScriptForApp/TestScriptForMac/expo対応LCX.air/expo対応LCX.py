# -*- encoding=utf8 -*-
__author__ = "joseishou"

import time

from airtest.core.api import *
from airtest.report.report import simple_report

auto_setup(__file__, logdir=True, devices=["ios:///127.0.0.1:8100"])


def keyboard_open():
    touch(Template(r"tpl1685340995489.png", record_pos=(-0.291, -0.346), resolution=(2160, 1620)))  # "キーボード"を開く
    time.sleep(3)


def research():
    touch(Template(r"tpl1708923177179.png", record_pos=(0.351, -0.27), resolution=(2160, 1620)))  # "再検索"をタップ
    time.sleep(5)


def enter_key():
    touch(Template(r"tpl1708927376123.png", record_pos=(0.423, 0.172), resolution=(2160, 1620)))
    time.sleep(5)


dev = device()
dev.start_recording(output="test.mp4", max_time="36000", orientation=2)
try:
    for times in range(5):
        start_app("jp.co.couger.ludens")  # アプリ起動する
        time.sleep(10)

        text("12qwaszx!", enter=False)  # パスワード入力する
        time.sleep(3)

        touch(Template(r"tpl1684723341307.png", record_pos=(0.001, -0.106), resolution=(2160, 1620)))  # "OK"ボタンをクリックする
        time.sleep(10)

        if exists(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620))):  # ダイアログ判断
            touch(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620)))  # 画面転移キャンセル5
            time.sleep(2)

        touch(Template(r"tpl1685340943532.png", record_pos=(-0.471, -0.344), resolution=(2160, 1620)))  # "キーボード"ボタンをクリックする
        time.sleep(3)

        keyboard_open()
        text("おはよう", enter=False)
        time.sleep(3)
        enter_key()
        time.sleep(10)

        keyboard_open()
        text("お疲れ様", enter=False)
        time.sleep(3)
        enter_key()
        time.sleep(10)

        keyboard_open()
        text("業務マニュアル", enter=False)
        time.sleep(3)
        enter_key()

        wait(Template(r"tpl1708937862818.png", record_pos=(-0.074, -0.269), resolution=(2160, 1620)))
        keyboard_open()
        text("返金のやり方を教えて", enter=False)
        time.sleep(3)
        enter_key()

        touch(Template(r"tpl1709010090125.png", record_pos=(0.39, -0.174), resolution=(2160, 1620)))  # "詳しく見る"をタップ
        time.sleep(10)

        touch(Template(r"tpl1708950917102.png", record_pos=(-0.469, -0.355), resolution=(2160, 1620)))  # "完了"をタップ
        time.sleep(5)

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        wait(Template(r"tpl1708926342348.png", record_pos=(0.264, -0.23), resolution=(2160, 1620)))
        keyboard_open()
        text("前日のデータ", enter=False)
        time.sleep(3)
        enter_key()

        wait(Template(r"tpl1708938869365.png", record_pos=(-0.024, -0.161), resolution=(2160, 1620)))
        keyboard_open()
        text("前日", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("翌日", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("廃棄予算設定", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("自分の記録", enter=False)
        time.sleep(3)
        enter_key()

        for times1 in range(2):
            keyboard_open()
            text("閉じる", enter=False)
            time.sleep(3)
            enter_key()

        keyboard_open()
        text("発注ポイント", enter=False)
        time.sleep(3)
        enter_key()

        if exists(Template(r"tpl1708950434156.png", record_pos=(0.391, -0.215), resolution=(2160, 1620))):
            keyboard_open()
            text("一番のマーケティングニュース", enter=False)
            time.sleep(3)
            enter_key()
            touch(Template(r"tpl1708951435578.png", record_pos=(-0.468, -0.355), resolution=(2160, 1620)))
            time.sleep(3)
            keyboard_open()
            text("寿司の品揃え", enter=False)
            time.sleep(3)
            enter_key()
            keyboard_open()
            text("月間実績", enter=False)
            time.sleep(3)
            enter_key()
            keyboard_open()
            text("閉じる", enter=False)
            time.sleep(3)
            enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        wait(Template(r"tpl1708952054636.png", record_pos=(0.268, -0.091), resolution=(2160, 1620)))
        keyboard_open()
        text("やることリスト", enter=False)
        time.sleep(3)
        enter_key()

        if exists(Template(r"tpl1708953258292.png", record_pos=(0.414, -0.089), resolution=(2160, 1620))):
            touch(Template(r"tpl1708953258292.png", record_pos=(0.414, -0.089), resolution=(2160, 1620)))  # チェックボックスをタップ
            time.sleep(3)
            touch(
                Template(r"tpl1708953311292.png", record_pos=(0.414, -0.089), resolution=(2160, 1620)))  # もう一回チェックボックスをタップ
            time.sleep(3)

        keyboard_open()
        text("事前発注", enter=False)
        time.sleep(3)
        enter_key()

        if exists(Template(r"tpl1708953258292.png", record_pos=(0.414, -0.089), resolution=(2160, 1620))):
            touch(Template(r"tpl1709016798936.png", record_pos=(0.416, -0.194), resolution=(2160, 1620)))  # チェックボックスをタップ
            time.sleep(3)
            touch(
                Template(r"tpl1709016816560.png", record_pos=(0.415, -0.192), resolution=(2160, 1620)))  # もう一回チェックボックスをタップ
            time.sleep(3)

        keyboard_open()
        text("オペレーション", enter=False)
        time.sleep(3)
        enter_key()

        if exists(Template(r"tpl1708953516948.png", record_pos=(0.391, -0.184), resolution=(2160, 1620))):
            touch(Template(r"tpl1708953516948.png", record_pos=(0.391, -0.184), resolution=(2160, 1620)))  # マーケティングニュースをタップ
            time.sleep(5)
            touch((0.034, 0.029))  # マーケティングニュースを閉じる
            time.sleep(3)
            touch(Template(r"tpl1708959672733.png", record_pos=(0.312, -0.102), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1708959695324.png", record_pos=(0.314, -0.104), resolution=(2160, 1620)))
            time.sleep(3)

        if exists(Template(r"tpl1703233590913.png", record_pos=(0.393, 0.324), resolution=(2160, 1620))):
            touch(Template(r"tpl1703233590913.png", record_pos=(0.393, 0.324), resolution=(2160, 1620)))  # 写真を送るをタップ
            time.sleep(3)
            keyboard_open()
            text("閉じる", enter=False)
            time.sleep(3)
            enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("ウィークリーポイント", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("ウィークリーポイント", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("前週", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("次週", enter=False)
        time.sleep(3)
        enter_key()

        if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
            keyboard_open()
            text("一番のマーケティングニュース", enter=False)
            time.sleep(3)
            enter_key()
            touch((0.034, 0.029))  # マーケティングニュースを閉じる
            time.sleep(3)

        if exists(Template(r"tpl1708957230053.png", record_pos=(0.409, -0.095), resolution=(2160, 1620))):
            keyboard_open()
            text("新商品案内", enter=False)
            time.sleep(3)
            enter_key()
            if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
                touch(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620)))
                time.sleep(5)
                touch((0.034, 0.029))  # マーケティングニュースを閉じる
                time.sleep(3)

        if exists(Template(r"tpl1708957477959.png", record_pos=(0.413, -0.04), resolution=(2160, 1620))):
            keyboard_open()
            text("今お得", enter=False)
            time.sleep(3)
            enter_key()
            if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
                keyboard_open()
                text("一番のマーケティングニュース", enter=False)
                time.sleep(3)
                enter_key()
                touch((0.034, 0.029))  # マーケティングニュースを閉じる
                time.sleep(3)

        if exists(Template(r"tpl1708958113834.png", record_pos=(0.412, 0.016), resolution=(2160, 1620))):
            keyboard_open()
            text("事前発注", enter=False)
            time.sleep(3)
            enter_key()
            if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
                keyboard_open()
                text("一番のマーケティングニュース", enter=False)
                time.sleep(3)
                enter_key()
                touch((0.034, 0.029))  # マーケティングニュースを閉じる
                time.sleep(3)

        if exists(Template(r"tpl1709000610821.png", record_pos=(0.411, 0.072), resolution=(2160, 1620))):
            keyboard_open()
            text("1個もらえる企画", enter=False)
            time.sleep(3)
            enter_key()
            if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
                keyboard_open()
                text("一番のマーケティングニュース", enter=False)
                time.sleep(3)
                enter_key()
                touch((0.034, 0.029))  # マーケティングニュースを閉じる
                time.sleep(3)

        if exists(Template(r"tpl1709000926416.png", record_pos=(0.41, 0.129), resolution=(2160, 1620))):
            keyboard_open()
            text("レシートクーポン", enter=False)
            time.sleep(3)
            enter_key()
            if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
                keyboard_open()
                text("一番のマーケティングニュース", enter=False)
                time.sleep(3)
                enter_key()
                touch((0.034, 0.029))  # マーケティングニュースを閉じる
                time.sleep(3)

        if exists(Template(r"tpl1709001158828.png", record_pos=(0.412, 0.184), resolution=(2160, 1620))):
            keyboard_open()
            text("指定返品", enter=False)
            time.sleep(3)
            enter_key()
            if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
                keyboard_open()
                text("一番のマーケティングニュース", enter=False)
                time.sleep(3)
                enter_key()
                touch((0.034, 0.029))  # マーケティングニュースを閉じる
                time.sleep(3)

        if exists(Template(r"tpl1709001460103.png", record_pos=(0.41, 0.239), resolution=(2160, 1620))):
            keyboard_open()
            text("オペレーション", enter=False)
            time.sleep(3)
            enter_key()
            if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
                keyboard_open()
                text("一番のマーケティングニュース", enter=False)
                time.sleep(3)
                enter_key()
                touch((0.034, 0.029))  # マーケティングニュースを閉じる
                time.sleep(3)

        if exists(Template(r"tpl1709001521805.png", record_pos=(0.409, 0.291), resolution=(2160, 1620))):
            keyboard_open()
            text("連絡事項", enter=False)
            time.sleep(3)
            enter_key()
            if exists(Template(r"tpl1708957088675.png", record_pos=(0.261, -0.215), resolution=(2160, 1620))):
                keyboard_open()
                text("二番のマーケティングニュース", enter=False)
                time.sleep(3)
                enter_key()
                touch((0.034, 0.029))  # マーケティングニュースを閉じる
                time.sleep(3)
            keyboard_open()
            text("SVから", enter=False)
            time.sleep(3)
            enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        wait(Template(r"tpl1709002259878.png", record_pos=(0.304, 0.097), resolution=(2160, 1620)))
        keyboard_open()
        text("前週のレビュー", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("中食のレビュー", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("前週", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("次週", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("調理パン", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("調理パンの品揃え", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("デザート", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("その他デザート", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("月間実績", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("パン", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("惣菜パン", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("前週", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("次週", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("キャンペーン情報", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("トップ画面に戻る", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("自分の記録", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("販売ランキング", enter=False)
        time.sleep(3)
        enter_key()

        for times2 in range(2):
            keyboard_open()
            text("前週", enter=False)
            time.sleep(3)
            enter_key()
        for times3 in range(2):
            keyboard_open()
            text("次週", enter=False)
            time.sleep(3)
            enter_key()

        keyboard_open()
        text("おむすびのランキングを見せて", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("売場の写真", enter=False)
        time.sleep(3)
        enter_key()

        touch((0.468, 0.264))  # 写真をタップ
        time.sleep(3)

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()
        """
        for time4 in range(2):
            keyboard_open()
            text("次へ",enter = False)
            time.sleep(3)
            enter_key()
    
        keyboard_open()
        text("前へ",enter = False)
        time.sleep(3)
        enter_key()
    
        keyboard_open()
        text("最初に戻る",enter = False)
        time.sleep(3)
        enter_key()
        """
        keyboard_open()
        text("自店の写真", enter=False)
        time.sleep(3)
        enter_key()

        touch((0.468, 0.264))  # 写真をタップ
        time.sleep(3)

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()
        """
        for time5 in range(2):
            keyboard_open()
            text("次へ",enter = False)
            time.sleep(3)
            enter_key()
    
        keyboard_open()
        text("前へ",enter = False)
        time.sleep(3)
        enter_key()
    
        keyboard_open()
        text("最初に戻る",enter = False)
        time.sleep(3)
        enter_key()
        """
        keyboard_open()
        text("みんなの写真", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        wait(Template(r"tpl1708926342348.png", record_pos=(0.264, -0.23), resolution=(2160, 1620)))
        keyboard_open()
        text("チャンスロス", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("前日", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("翌日", enter=False)
        time.sleep(3)
        enter_key()

        touch(Template(r"tpl1709008449685.png", record_pos=(0.387, -0.145), resolution=(2160, 1620)))  # 時間帯で見るをタップ
        time.sleep(3)

        keyboard_open()
        text("前日", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("翌日", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("調理麺", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("パスタ", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        keyboard_open()
        text("閉じる", enter=False)
        time.sleep(3)
        enter_key()

        stop_app("jp.co.couger.ludens")  # アプリを閉じる
        time.sleep(3)
finally:
    dev.stop_recording()
    simple_report(__file__, logpath=True)
