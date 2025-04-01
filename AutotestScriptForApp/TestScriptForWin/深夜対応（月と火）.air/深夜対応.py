# -*- encoding=utf8 -*-
__author__ = "joseishou"

from airtest.core.api import *
from airtest.report.report import simple_report

auto_setup(__file__, logdir=True, devices=["ios:///127.0.0.1:8100"])

dev = device()
dev.start_recording(output="test.mp4", max_time="36000", orientation=2)

try:
    start_app("jp.co.couger.ludens")  # アプリ起動する
    time.sleep(10)
    text("12qwaszx!", enter=False)  # パスワード入力する
    time.sleep(3)
    touch(Template(r"tpl1684723341307.png", record_pos=(0.001, -0.106), resolution=(2160, 1620)))  # "OK"ボタンをクリックする
    time.sleep(12)    
    touch(Template(r"tpl1710771512317.png", record_pos=(0.433, -0.28), resolution=(2160, 1620)))
    time.sleep(5)
        
    try:
        for times in range(10000):
            touch(Template(r"tpl1706452427991.png", record_pos=(0.273, -0.09), resolution=(2160, 1620)))  # やることリストをタップ
            time.sleep(5)
            touch(Template(r"tpl1709218430377.png", record_pos=(-0.161, -0.122), resolution=(2160, 1620)))  # 商品コードを開く
            time.sleep(5)
            touch((0.166, 0.471))  # 商品コードを閉じる
            time.sleep(5)
            touch(Template(r"tpl1709217432589.png", record_pos=(0.416, -0.142), resolution=(2160, 1620)))  # 対応済み
            time.sleep(5)
            touch(Template(r"tpl1709217466992.png", record_pos=(0.415, -0.141), resolution=(2160, 1620)))  # 対応済みキャンセル
            time.sleep(5)
            touch(Template(r"tpl1709217534553.png", record_pos=(-0.053, -0.275), resolution=(2160, 1620)))  # 事前発注をタップ
            time.sleep(5)
            
            if exists(Template(r"tpl1709217583418.png", record_pos=(0.414, -0.193), resolution=(2160, 1620))):
                touch(Template(r"tpl1709217583418.png", record_pos=(0.414, -0.193), resolution=(2160, 1620)))  # 対応済み
                time.sleep(5)
                touch(Template(r"tpl1709217622573.png", record_pos=(0.415, -0.193), resolution=(2160, 1620)))  # 対応済みキャンセル
                time.sleep(5)

            touch(Template(r"tpl1709217702182.png", record_pos=(0.092, -0.274), resolution=(2160, 1620)))  # オペレーションをタップ
            time.sleep(5)
            touch(Template(r"tpl1709718942713.png", record_pos=(0.313, -0.102), resolution=(2160, 1620)))  # 対応済み
            time.sleep(5)
            touch(Template(r"tpl1709718974254.png", record_pos=(0.312, -0.101), resolution=(2160, 1620)))  # 対応済みキャンセル
            time.sleep(5)
            touch(Template(r"tpl1709719015466.png", record_pos=(0.39, -0.185),
                           resolution=(2160, 1620)))  # マーケティングニュースをタップ
            time.sleep(5)
            touch(Template(r"tpl1709719158767.png", record_pos=(-0.469, -0.356), resolution=(2160, 1620)))  # 完了をタップ
            time.sleep(5)
            if exists(Template(r"tpl1703233590913.png", record_pos=(0.393, 0.324), resolution=(2160, 1620))):
                touch(Template(r"tpl1703233590913.png", record_pos=(0.393, 0.324), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1703233667528.png", record_pos=(-0.002, 0.239), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1703233687944.png", record_pos=(-0.181, 0.255), resolution=(2160, 1620)))
                time.sleep(5)
                touch((0.401, 0.31))
                time.sleep(5)
                touch(Template(r"tpl1703233757244.png", record_pos=(0.287, -0.333), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1703233772548.png", record_pos=(0.0, 0.304), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1703233794848.png", record_pos=(0.389, 0.323), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1703233811762.png", record_pos=(0.282, -0.271), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1703233825827.png", record_pos=(0.341, -0.237), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1703233841711.png", record_pos=(0.07, 0.057), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1703233858044.png", record_pos=(0.452, -0.283), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1685007281563.png", record_pos=(0.43, -0.282), resolution=(2160, 1620)))  # トップメニューに戻る
                time.sleep(10)
                touch(Template(r"tpl1709719231805.png", record_pos=(0.29, 0.016),
                               resolution=(2160, 1620)))  # weekly pointをタップ
                time.sleep(5)
                touch(Template(r"tpl1710222435370.png", record_pos=(0.413, -0.247), resolution=(2160, 1620)))
                time.sleep(5)
                touch(Template(r"tpl1709719465834.png", record_pos=(-0.468, -0.356), resolution=(2160, 1620)))  # 完了をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709719792327.png", record_pos=(0.174, -0.216), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709719792327.png", record_pos=(0.174, -0.216),
                                   resolution=(2160, 1620)))  # 概要をタップ
                    time.sleep(5)
                    touch(Template(r"tpl1709719792327.png", record_pos=(0.174, -0.216), resolution=(2160, 1620)))
                    time.sleep(5)
                if exists(Template(r"tpl1709720091110.png", record_pos=(0.261, -0.214), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720091110.png", record_pos=(0.261, -0.214), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720341319.png", record_pos=(-0.469, -0.356),
                                   resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)

                touch(Template(r"tpl1709720408953.png", record_pos=(0.409, -0.094), resolution=(2160, 1620)))  # 新商品案内をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),
                                   resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)

                touch(Template(r"tpl1709720601182.png", record_pos=(0.407, -0.04), resolution=(2160, 1620)))  # 今お得をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709720664614.png", record_pos=(0.245, -0.284), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720664614.png", record_pos=(0.245, -0.284), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720719135.png", record_pos=(-0.468, -0.356),
                                   resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)
                if exists(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),
                                   resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)

                touch(Template(r"tpl1709720773446.png", record_pos=(0.389, 0.016), resolution=(2160, 1620)))  # 事前発注をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)
                    touch(Template(r"tpl1710223843090.png", record_pos=(0.244, -0.282), resolution=(2160, 1620)))   # 全ての事前発注を見る
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)
                touch(Template(r"tpl1709720950241.png", record_pos=(0.409, 0.071), resolution=(2160, 1620)))  # 一個もらえるをタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),
                                   resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)

                touch(Template(r"tpl1709721017576.png", record_pos=(0.41, 0.127),
                               resolution=(2160, 1620)))  # レシートクーポンをタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),
                                   resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)

                touch(Template(r"tpl1709721096415.png", record_pos=(0.407, 0.182), resolution=(2160, 1620)))  # 指定返品をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),
                                   resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)

                touch(Template(r"tpl1709721168273.png", record_pos=(0.408, 0.236),
                               resolution=(2160, 1620)))  # オペレーションをタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),
                                   resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)

                touch(Template(r"tpl1709721223554.png", record_pos=(0.411, 0.293), resolution=(2160, 1620)))  # 連絡事項をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                if exists(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620))):
                    touch(Template(r"tpl1709720461050.png", record_pos=(0.26, 0.006), resolution=(2160, 1620)))
                    time.sleep(5)
                    touch(Template(r"tpl1709720533982.png", record_pos=(-0.468, -0.356),resolution=(2160, 1620)))  # 完了をタップ
                    time.sleep(5)
                touch(Template(r"tpl1709721285669.png", record_pos=(-0.082, -0.274), resolution=(2160, 1620)))  # svからをタップ
                time.sleep(5)
                touch(Template(r"tpl1709721387553.png", record_pos=(0.37, -0.275), resolution=(2160, 1620)))  # 前週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721408911.png", record_pos=(0.458, -0.274), resolution=(2160, 1620)))  # 次週をタップ
                time.sleep(5)
                touch(Template(r"tpl1709721607184.png", record_pos=(0.459, -0.335), resolution=(2160, 1620)))
                time.sleep(10)
                
    finally:
        stop_app("jp.co.couger.ludens")
        time.sleep(7260)
        start_app("jp.co.couger.ludens")
        time.sleep(12)
        text("12qwaszx!", enter=False)  # パスワード入力する
        time.sleep(3)
        touch(Template(r"tpl1684723341307.png", record_pos=(0.001, -0.106), resolution=(2160, 1620)))  # "OK"ボタンをクリックする
        time.sleep(12)
        if exists(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620))):  # ダイアログ判断
            touch(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620)))  # 画面転移キャンセル5
            time.sleep(2)
        time.sleep(3)

finally:
    dev.stop_recording()
    simple_report(__file__, logpath=True)
