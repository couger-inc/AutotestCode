# -*- encoding=utf8 -*-
__author__ = "shengqing"

from airtest.core.api import *
from airtest.report.report import simple_report

auto_setup(__file__, logdir=True, devices=["ios:///127.0.0.1:8100"])

dev = device()

dev.start_recording(output="test.mp4", max_time="36000", orientation=2)

try:
    for times in range(1):
        start_app("jp.co.couger.ludens")  #アプリ起動する
        time.sleep(10)
        text("12qwaszx!", enter=False)  #パスワード入力する
        time.sleep(3)
        touch(Template(r"tpl1684723341307.png", record_pos=(0.001, -0.106), resolution=(2160, 1620)))  #"OK"ボタンをクリックする
        time.sleep(12)
        if exists(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620))):  #ダイアログ判断
            touch(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620)))  #画面転移キャンセル5
            time.sleep(2)
        touch(Template(r"tpl1684731168165.png", record_pos=(0.304, -0.204), resolution=(2160, 1620)))  #"前日のデータ"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1692955091239.png", record_pos=(0.287, -0.266), resolution=(2160, 1620)))  #"前日"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1692955132104.png", record_pos=(0.368, -0.267), resolution=(2160, 1620)))  #"翌日"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684732644173.png", record_pos=(-0.009, 0.237), resolution=(2160, 1620)))  #"自分の記録"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684733458561.png", record_pos=(0.431, -0.274), resolution=(2160, 1620)))  #"自分の記録"から"前日のデータ"に戻る
        time.sleep(3)
        touch(Template(r"tpl1684734179239.png", record_pos=(0.398, 0.238), resolution=(2160, 1620)))  #"廃棄予算設定"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684741923413.png", record_pos=(0.069, 0.03), resolution=(2160, 1620)))  #"原価"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684744375520.png", record_pos=(0.353, 0.093), resolution=(2160, 1620)))  #"AC"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684742712322.png", record_pos=(0.185, 0.046), resolution=(2160, 1620)))  #"1"をクリックする
        time.sleep(3)
        touch(Template(r"tpl1684742854268.png", record_pos=(0.318, 0.215), resolution=(2160, 1620)))  #"設定する"ボタンをクリックする("前日のデータ"画面に戻る)
        time.sleep(3)
        touch(Template(r"tpl1684734179239.png", record_pos=(0.398, 0.238), resolution=(2160, 1620)))  #"廃棄予算設定"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684742139381.png", record_pos=(0.002, 0.029), resolution=(2160, 1620)))  #"売価"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684744375520.png", record_pos=(0.353, 0.093), resolution=(2160, 1620)))  #"AC"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684742712322.png", record_pos=(0.185, 0.046), resolution=(2160, 1620)))  #"1"をクリックする
        time.sleep(3)
        touch(Template(r"tpl1684742854268.png", record_pos=(0.318, 0.215), resolution=(2160, 1620)))  #"設定する"ボタンをクリックする("前日のデータ"画面に戻る)
        time.sleep(3)
        touch(Template(r"tpl1684734179239.png", record_pos=(0.398, 0.238), resolution=(2160, 1620)))  #"廃棄予算設定"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684744498044.png", record_pos=(0.069, 0.216), resolution=(2160, 1620)))  #"キャンセル"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684744582351.png", record_pos=(0.381, 0.174), resolution=(2160, 1620)))  #"カテゴリー"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684991707801.png", record_pos=(0.385, -0.144), resolution=(2160, 1620)))  #"時間帯で見る"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684748842298.png", record_pos=(-0.423, 0.294), resolution=(2160, 1620)))  #"客数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684812715677.png", record_pos=(-0.422, 0.294), resolution=(2160, 1620)))  #もう一度"客数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684820079082.png", record_pos=(-0.335, 0.294), resolution=(2160, 1620)))  #"中食の購入者数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684820727322.png", record_pos=(-0.336, 0.294), resolution=(2160, 1620)))  #もう一度"中食の購入者数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684820773876.png", record_pos=(-0.192, 0.294), resolution=(2160, 1620)))  #"当カテゴリーの購入者数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684820931535.png", record_pos=(-0.191, 0.294), resolution=(2160, 1620)))  #もう一度"当カテゴリーの購入者数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684821105417.png", record_pos=(-0.269, -0.231), resolution=(2160, 1620)))  #左のプルダウンメニューを開く
        time.sleep(3)
        touch(Template(r"tpl1684821105417.png", record_pos=(-0.269, -0.231), resolution=(2160, 1620)))  #左のプルダウンメニューを閉じる
        time.sleep(3)
        touch(Template(r"tpl1684821159094.png", record_pos=(-0.073, -0.231), resolution=(2160, 1620)))  #右のプルダウンメニューを開く
        time.sleep(3)
        touch(Template(r"tpl1684821159094.png", record_pos=(-0.073, -0.231), resolution=(2160, 1620)))  #右のプルダウンメニューを閉じる
        time.sleep(3)
        touch(Template(r"tpl1684821690210.png", record_pos=(0.441, -0.274), resolution=(2160, 1620)))  #"カテゴリー"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1684826810583.png", record_pos=(0.283, -0.28), resolution=(2160, 1620)))  #"前日"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684826838188.png", record_pos=(0.364, -0.277), resolution=(2160, 1620)))  #"翌日"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684833709238.png", record_pos=(0.431, -0.281), resolution=(2160, 1620)))  #"前日のデータ"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1684835640782.png", record_pos=(0.433, -0.281), resolution=(2160, 1620)))  #"ホームページ"に戻る
        time.sleep(3)
        touch(Template(r"tpl1684911401105.png", record_pos=(0.305, -0.133), resolution=(2160, 1620)))  #"発注ポイント"ボタンをクリックする
        time.sleep(3)

        if exists(Template(r"tpl1684913480910.png", record_pos=(0.303, -0.216), resolution=(2160, 1620))):  #"重要施策"画面で内容があるかどうかの判断のため

            touch(Template(r"tpl1684911585486.png", record_pos=(0.304, -0.216), resolution=(2160, 1620)))  #"概要"ボタンをクリックする("概要"tipsを開く)
            time.sleep(3)
            touch(Template(r"tpl1684911669355.png", record_pos=(0.305, -0.217), resolution=(2160, 1620)))  #もう一度"概要"ボタンをクリックする("概要"tipsを閉じる)
            time.sleep(3)
            # touch(Template(r"tpl1684911851340.png", record_pos=(0.39, -0.214), resolution=(2160, 1620)))  #"マーケティングニュース"ボタンをクリックする
            # time.sleep(3)
            # touch(Template(r"tpl1684911969947.png", record_pos=(-0.467, -0.354), resolution=(2160, 1620)))  #"完了"ボタンをクリックする
            time.sleep(3)
            touch(Template(r"tpl1684915412883.png", record_pos=(0.313, -0.147), resolution=(2160, 1620)))  #"品揃え"ボタンをクリックする
            time.sleep(3)
            touch(Template(r"tpl1684916277771.png", record_pos=(0.444, -0.274), resolution=(2160, 1620)))  #"重要施策"画面に戻る
            time.sleep(3)
            touch(Template(r"tpl1684921063632.png", record_pos=(0.389, -0.101), resolution=(2160, 1620)))  #"個数"ボタンをクリックする
            time.sleep(3)
            touch(Template(r"tpl1684921117151.png", record_pos=(0.314, -0.101), resolution=(2160, 1620)))  #"金額"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1685325545745.png", record_pos=(0.443, -0.275), resolution=(2160, 1620)))  #"トップメニュー"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1685004456339.png", record_pos=(0.301, -0.065), resolution=(2160, 1620)))  #"やることリスト"ボタンをクリックする
        time.sleep(3)
        if exists(Template(r"tpl1685342264082.png", record_pos=(-0.163, 0.202), resolution=(2160, 1620))):
            touch(Template(r"tpl1685005519851.png", record_pos=(-0.159, -0.12), resolution=(2160, 1620)))  #"商品コード"tips開く
            time.sleep(3)
            touch(Template(r"tpl1685005773099.png", record_pos=(-0.457, -0.294), resolution=(2160, 1620)))  #"商品コード"tips閉じる
            time.sleep(3)
        if exists(Template(r"tpl1685005870209.png", record_pos=(0.417, -0.139), resolution=(2160, 1620))):
            touch(Template(r"tpl1685005870209.png", record_pos=(0.417, -0.139), resolution=(2160, 1620)))  #"対応済"
            time.sleep(3)
            touch(Template(r"tpl1685005986322.png", record_pos=(0.416, -0.14), resolution=(2160, 1620)))  #"対応済"キャンセルする
            time.sleep(3)
        touch(Template(r"tpl1685006124970.png", record_pos=(-0.05, -0.274), resolution=(2160, 1620)))  #"事前発注"画面を開く
        time.sleep(3)
        if exists(Template(r"tpl1685006323268.png", record_pos=(0.415, -0.193), resolution=(2160, 1620))):  #画面て内容の有無の判断
            touch(Template(r"tpl1685006347944.png", record_pos=(0.415, -0.194), resolution=(2160, 1620)))  #"対応済"
            time.sleep(3)
            touch(Template(r"tpl1685328323476.png", record_pos=(0.415, -0.193), resolution=(2160, 1620)))  #"対応済"キャンセル
            time.sleep(3)
        touch(Template(r"tpl1685006638434.png", record_pos=(0.094, -0.276), resolution=(2160, 1620)))  #"オペレーション"画面を開く
        time.sleep(3)
        touch(Template(r"tpl1709255376543.png", record_pos=(0.312, -0.103), resolution=(2160, 1620)))  # 対応済み
        time.sleep(3)
        touch(Template(r"tpl1709255417639.png", record_pos=(0.312, -0.102), resolution=(2160, 1620)))  # 対応済み
        time.sleep(3)
        touch(Template(r"tpl1709255457186.png", record_pos=(0.392, -0.183), resolution=(2160, 1620)))  #"マーケティングニュース"を開く
        time.sleep(3)
        touch(Template(r"tpl1685006991740.png", record_pos=(-0.469, -0.355), resolution=(2160, 1620)))  #"オペレーション"画面に戻る
        time.sleep(3)

        if exists(Template(r"tpl1703233590913.png", record_pos=(0.393, 0.324), resolution=(2160, 1620))):
            touch(Template(r"tpl1703233590913.png", record_pos=(0.393, 0.324), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1703233667528.png", record_pos=(-0.002, 0.239), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1703233687944.png", record_pos=(-0.181, 0.255), resolution=(2160, 1620)))
            time.sleep(3)
            touch((0.401, 0.31))
            time.sleep(3)
            touch(Template(r"tpl1703233757244.png", record_pos=(0.287, -0.333), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1703233772548.png", record_pos=(0.0, 0.304), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1703233794848.png", record_pos=(0.389, 0.323), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1703233811762.png", record_pos=(0.282, -0.271), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1703233825827.png", record_pos=(0.341, -0.237), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1703233841711.png", record_pos=(0.07, 0.057), resolution=(2160, 1620)))
            time.sleep(3)
            touch(Template(r"tpl1703233858044.png", record_pos=(0.452, -0.283), resolution=(2160, 1620)))
            time.sleep(3)
        else:
            swipe((0.57, 0.95), (0.57, 0.25))
            time.sleep(3)
            if exists(Template(r"tpl1703233590913.png", record_pos=(0.393, 0.324), resolution=(2160, 1620))):
                touch(Template(r"tpl1703233590913.png", record_pos=(0.393, 0.324), resolution=(2160, 1620)))
                time.sleep(3)
                touch(Template(r"tpl1703233667528.png", record_pos=(-0.002, 0.239), resolution=(2160, 1620)))
                time.sleep(3)
                touch(Template(r"tpl1703233687944.png", record_pos=(-0.181, 0.255), resolution=(2160, 1620)))
                time.sleep(3)
                touch((0.401, 0.31))
                time.sleep(3)
                touch(Template(r"tpl1703233757244.png", record_pos=(0.287, -0.333), resolution=(2160, 1620)))
                time.sleep(3)
                touch(Template(r"tpl1703233772548.png", record_pos=(0.0, 0.304), resolution=(2160, 1620)))
                time.sleep(3)
                touch(Template(r"tpl1703233794848.png", record_pos=(0.389, 0.323), resolution=(2160, 1620)))
                time.sleep(3)
                touch(Template(r"tpl1703233811762.png", record_pos=(0.282, -0.271), resolution=(2160, 1620)))
                time.sleep(3)
                touch(Template(r"tpl1703233825827.png", record_pos=(0.341, -0.237), resolution=(2160, 1620)))
                time.sleep(3)
                touch(Template(r"tpl1703233841711.png", record_pos=(0.07, 0.057), resolution=(2160, 1620)))
                time.sleep(3)
                touch(Template(r"tpl1703233858044.png", record_pos=(0.452, -0.283), resolution=(2160, 1620)))
                time.sleep(3)

        touch(Template(r"tpl1685007281563.png", record_pos=(0.43, -0.282), resolution=(2160, 1620)))  #トップメニューに戻る
        time.sleep(3)
        touch(Template(r"tpl1685069011697.png", record_pos=(0.305, 0.055), resolution=(2160, 1620)))  #"Weekly Point"ボタンをクリックする
        time.sleep(3)
        if exists(Template(r"tpl1685069426386.png", record_pos=(0.175, -0.217), resolution=(2160, 1620))):
            touch(Template(r"tpl1685069426386.png", record_pos=(0.175, -0.217), resolution=(2160, 1620)))  #"概要"をクリックする
            time.sleep(3)
            touch(Template(r"tpl1685069685588.png", record_pos=(0.172, -0.216), resolution=(2160, 1620)))  #"概要"tipsを閉じる
            time.sleep(3)
            touch(Template(r"tpl1707897411250.png", record_pos=(0.262, -0.147), resolution=(2160, 1620)))  #"マーケティングニュース"ボタンをクリックする
            time.sleep(3)
            touch(Template(r"tpl1685069798146.png", record_pos=(-0.466, -0.356), resolution=(2160, 1620)))  #"Weekly Point"画面に戻る
            time.sleep(3)
        touch(Template(r"tpl1685070093488.png", record_pos=(0.368, -0.273), resolution=(2160, 1620)))  #"前週"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1685070147336.png", record_pos=(0.457, -0.274), resolution=(2160, 1620)))  #"次週"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1685070206066.png", record_pos=(0.411, -0.223), resolution=(2160, 1620)))  #"Weekly Point"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1685070434687.png", record_pos=(-0.469, -0.356), resolution=(2160, 1620)))  #"Weekly Point"画面に戻る
        time.sleep(3)
        if exists(Template(r"tpl1685070852135.png", record_pos=(0.402, -0.094), resolution=(2160, 1620))):
            touch(Template(r"tpl1685070868997.png", record_pos=(0.405, -0.094), resolution=(2160, 1620)))  #"新商品案内"
            time.sleep(3)
        if exists(Template(r"tpl1685071017639.png", record_pos=(0.402, -0.038), resolution=(2160, 1620))):
            touch(Template(r"tpl1685070973886.png", record_pos=(0.403, -0.038), resolution=(2160, 1620)))  #"今お得"
            time.sleep(3)
        if exists(Template(r"tpl1685071031482.png", record_pos=(0.401, 0.017), resolution=(2160, 1620))):
            touch(Template(r"tpl1685071053132.png", record_pos=(0.4, 0.016), resolution=(2160, 1620)))  #"事前発注"
            time.sleep(3)
        if exists(Template(r"tpl1685071104572.png", record_pos=(0.405, 0.071), resolution=(2160, 1620))):
            touch(Template(r"tpl1685071121620.png", record_pos=(0.405, 0.071), resolution=(2160, 1620)))  #"一個もらえる企画"
            time.sleep(3)
        if exists(Template(r"tpl1685071242138.png", record_pos=(0.406, 0.126), resolution=(2160, 1620))):
            touch(Template(r"tpl1685071259564.png", record_pos=(0.406, 0.126), resolution=(2160, 1620)))  #"レシートクーポン"
            time.sleep(3)
        if exists(Template(r"tpl1685071290911.png", record_pos=(0.401, 0.182), resolution=(2160, 1620))):
            touch(Template(r"tpl1685071305875.png", record_pos=(0.401, 0.181), resolution=(2160, 1620)))  #"指定返品"
            time.sleep(3)
        if exists(Template(r"tpl1685071342836.png", record_pos=(0.404, 0.237), resolution=(2160, 1620))):
            touch(Template(r"tpl1685071354264.png", record_pos=(0.403, 0.236), resolution=(2160, 1620)))  #"オペレーション"
            time.sleep(3)
        if exists(Template(r"tpl1685071395463.png", record_pos=(0.4, 0.292), resolution=(2160, 1620))):
            touch(Template(r"tpl1685071405139.png", record_pos=(0.401, 0.291), resolution=(2160, 1620)))  #"連絡事項"
            time.sleep(3)
            if exists(Template(r"tpl1690786704158.png", record_pos=(-0.08, -0.275), resolution=(2160, 1620))):
                touch(Template(r"tpl1690786704158.png", record_pos=(-0.08, -0.275), resolution=(2160, 1620)))  #"SVから"ボタンをクリック
                time.sleep(3)
                touch(Template(r"tpl1690787071256.png", record_pos=(-0.194, -0.275), resolution=(2160, 1620)))  #"本部から"をクリック
                time.sleep(3)
        touch(Template(r"tpl1685071528389.png", record_pos=(0.46, -0.336), resolution=(2160, 1620)))  #トップメニューに戻る
        time.sleep(3)
        touch(Template(r"tpl1687763946783.png", record_pos=(0.306, 0.097), resolution=(2160, 1620)))  #"前週のレビュー"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1687764053654.png", record_pos=(0.333, -0.218), resolution=(2160, 1620)))  #"中食中分類レビューを見る"ボタンをクリック
        time.sleep(3)
        touch(Template(r"tpl1690774209394.png", record_pos=(0.344, -0.217), resolution=(2160, 1620)))  #"前週"ボタンをクリック
        time.sleep(3)
        touch(Template(r"tpl1687914756774.png", record_pos=(0.378, -0.287), resolution=(2160, 1620)))  #"次週"ボタンをクリック
        time.sleep(3)
        touch(Template(r"tpl1687764502160.png", record_pos=(-0.189, -0.245), resolution=(2160, 1620)))  #"左の「？」ボタン"をクリック
        time.sleep(3)
        touch(Template(r"tpl1687764516518.png", record_pos=(-0.19, -0.245), resolution=(2160, 1620)))  #tipsを閉じる
        time.sleep(3)
        touch(Template(r"tpl1687764695228.png", record_pos=(0.244, -0.246), resolution=(2160, 1620)))  #"右の「？」ボタン"をクリック
        time.sleep(3)
        touch(Template(r"tpl1687764710239.png", record_pos=(0.244, -0.245), resolution=(2160, 1620)))  #tipsを閉じる
        time.sleep(3)
        touch(Template(r"tpl1687765191074.png", record_pos=(-0.237, -0.054), resolution=(2160, 1620)))  #"プールダウンメニュー"を開く
        time.sleep(3)
        touch(Template(r"tpl1687765206012.png", record_pos=(-0.236, -0.055), resolution=(2160, 1620)))  #"プールダウンメニュー"を閉じる
        time.sleep(3)
        if exists(Template(r"tpl1687765362070.png", record_pos=(-0.298, 0.064), resolution=(2160, 1620))):  #"施策情報"ボタンの有無を判断
            touch(Template(r"tpl1687765420691.png", record_pos=(-0.299, 0.065), resolution=(2160, 1620)))  #"施策情報"を開く
            time.sleep(3)
            touch(Template(r"tpl1687765579132.png", record_pos=(-0.298, 0.064), resolution=(2160, 1620)))  #"施策情報"を閉じる
            time.sleep(3)
        touch(Template(r"tpl1687765869392.png", record_pos=(0.304, -0.054), resolution=(2160, 1620)))  #"品揃え"ボタンをクリック
        time.sleep(3)
        touch(Template(r"tpl1690786002205.png", record_pos=(-0.428, 0.08), resolution=(2160, 1620)))  #"前週"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1690786011491.png", record_pos=(0.425, 0.079), resolution=(2160, 1620)))  #"次週"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684915601620.png", record_pos=(-0.297, -0.229), resolution=(2160, 1620)))  #左のプルダウンメニューを開く
        time.sleep(3)
        touch(Template(r"tpl1684915721586.png", record_pos=(-0.28, -0.23), resolution=(2160, 1620)))  #左のプルダウンメニューを閉じる
        time.sleep(3)
        touch(Template(r"tpl1684915744711.png", record_pos=(-0.078, -0.23), resolution=(2160, 1620)))  #右のプルダウンメニューを開く
        time.sleep(3)
        touch(Template(r"tpl1684915806955.png", record_pos=(-0.079, -0.23), resolution=(2160, 1620)))  #右のプルダウンメニューを閉じる
        time.sleep(3)
        touch(Template(r"tpl1687765895428.png", record_pos=(0.443, -0.275), resolution=(2160, 1620)))  #"中食中分類レビューを見る"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1690774280160.png", record_pos=(0.38, -0.055), resolution=(2160, 1620)))  #"月間実績"ボタンをクリック
        time.sleep(3)
        touch(Template(r"tpl1684919142176.png", record_pos=(-0.281, -0.266), resolution=(2160, 1620)))  #左のプルダウンメニューを開く
        time.sleep(3)
        touch(Template(r"tpl1684919194520.png", record_pos=(-0.277, -0.264), resolution=(2160, 1620)))  #左のプルダウンメニューを閉じる
        time.sleep(3)
        touch(Template(r"tpl1684919232429.png", record_pos=(-0.07, -0.266), resolution=(2160, 1620)))  #右のプルダウンメニューを開く
        time.sleep(3)
        touch(Template(r"tpl1685337724700.png", record_pos=(-0.061, -0.267), resolution=(2160, 1620)))  #右のプルダウンメニューを閉じる
        time.sleep(3)
        touch(Template(r"tpl1684920038954.png", record_pos=(-0.449, 0.149), resolution=(2160, 1620)))  #"前週"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920108528.png", record_pos=(0.449, 0.148), resolution=(2160, 1620)))  #"次週"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920191776.png", record_pos=(-0.424, 0.295), resolution=(2160, 1620)))  #"納品数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920281636.png", record_pos=(-0.424, 0.294), resolution=(2160, 1620)))  #もう一度"納品数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920330481.png", record_pos=(-0.323, 0.295), resolution=(2160, 1620)))  #"販売数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920376607.png", record_pos=(-0.325, 0.295), resolution=(2160, 1620)))  #もう一度"販売数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920450403.png", record_pos=(-0.225, 0.295), resolution=(2160, 1620)))  #"前年納品数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920509827.png", record_pos=(-0.225, 0.294), resolution=(2160, 1620)))  #もう一度"前年納品数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920576166.png", record_pos=(-0.106, 0.295), resolution=(2160, 1620)))  #"前年販売数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920629050.png", record_pos=(-0.106, 0.294), resolution=(2160, 1620)))  #もう一度"前年販売数"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920680064.png", record_pos=(0.374, 0.295), resolution=(2160, 1620)))  #"キャンペン情報"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1684920735776.png", record_pos=(0.371, 0.295), resolution=(2160, 1620)))  #もう一度"キャンペン情報"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1687766139955.png", record_pos=(0.444, -0.275), resolution=(2160, 1620)))  #"中食中分類レビューを見る"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1687766230296.png", record_pos=(0.455, -0.287), resolution=(2160, 1620)))  #"前週のレビュー"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1687766334147.png", record_pos=(0.245, 0.138), resolution=(2160, 1620)))  #"自店"ボタンを閉じろ
        time.sleep(3)
        touch(Template(r"tpl1687768258244.png", record_pos=(0.246, 0.137), resolution=(2160, 1620)))  #"自店"ボタンを開く
        time.sleep(3)
        touch(Template(r"tpl1687768494250.png", record_pos=(0.332, 0.139), resolution=(2160, 1620)))  #"営業所平均"ボタンを閉じる
        time.sleep(3)
        touch(Template(r"tpl1687768553099.png", record_pos=(0.331, 0.138), resolution=(2160, 1620)))  #"営業所平均"ボタンを開く
        time.sleep(3)
        swipe(Template(r"tpl1687768621282.png", record_pos=(-0.042, 0.134), resolution=(2160, 1620)), vector=[0.0149, -0.4191])  #画面を下にスワイプ
        time.sleep(3)
        touch(Template(r"tpl1687768832295.png", record_pos=(0.117, 0.013), resolution=(2160, 1620)))  #"中食の納品額"の折れ線表示を閉じる
        time.sleep(3)
        touch(Template(r"tpl1687768840775.png", record_pos=(0.117, 0.013), resolution=(2160, 1620)))  #"中食の納品額"の折れ線表示を開く
        time.sleep(3)
        touch(Template(r"tpl1687768994657.png", record_pos=(0.246, 0.013), resolution=(2160, 1620)))  #"中食の売上"の折れ線表示を閉じる
        time.sleep(3)
        touch(Template(r"tpl1687769056245.png", record_pos=(0.247, 0.014), resolution=(2160, 1620)))  #"中食の売上"の折れ線表示を開く
        time.sleep(3)
        touch(Template(r"tpl1687769094975.png", record_pos=(0.363, 0.013), resolution=(2160, 1620)))  #"客数"の折れ線表示を閉じる
        time.sleep(3)
        touch(Template(r"tpl1687769145481.png", record_pos=(0.361, 0.013), resolution=(2160, 1620)))  #"客数"の折れ線表示を開く
        time.sleep(3)
        swipe(Template(r"tpl1687769306176.png", record_pos=(-0.042, 0.013), resolution=(2160, 1620)), vector=[0.0041, 0.4461])  #画面を上にスワイプ
        time.sleep(3)
        touch(Template(r"tpl1687769370963.png", record_pos=(0.42, -0.28), resolution=(2160, 1620)))  #トップ画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1703257462236.png", record_pos=(0.198, 0.214), resolution=(2160, 1620)))  #"自分の記録"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1685071869528.png", record_pos=(0.433, -0.274), resolution=(2160, 1620)))  #トップメニューに戻る
        time.sleep(3)
        touch(Template(r"tpl1712021346745.png", record_pos=(0.269, 0.219), resolution=(2160, 1620)))  #"販売ランキング"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1690787464970.png", record_pos=(0.284, -0.28), resolution=(2160, 1620)))  #"前週"をクリック
        time.sleep(3)
        touch(Template(r"tpl1690787498221.png", record_pos=(0.363, -0.276), resolution=(2160, 1620)))  #"次週"をクリック
        time.sleep(3)
        touch(Template(r"tpl1685072068064.png", record_pos=(0.39, -0.158), resolution=(2160, 1620)))  #"ランキング"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1685072112506.png", record_pos=(0.434, -0.289), resolution=(2160, 1620)))  #"販売ランキング"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1685072162357.png", record_pos=(0.435, -0.279), resolution=(2160, 1620)))  #トップメニューに戻る
        time.sleep(3)
        touch(Template(r"tpl1685072366841.png", record_pos=(0.343, 0.18), resolution=(2160, 1620)))  #"売場の写真"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1685072414680.png", record_pos=(0.406, 0.218), resolution=(2160, 1620)))  #"次へ"
        time.sleep(3)
        touch(Template(r"tpl1685072422672.png", record_pos=(0.32, 0.219), resolution=(2160, 1620)))  #"前へ"
        time.sleep(3)
        touch(Template(r"tpl1685072434729.png", record_pos=(0.406, 0.218), resolution=(2160, 1620)))  #"次へ"
        time.sleep(3)
        touch(Template(r"tpl1685072441270.png", record_pos=(0.204, 0.219), resolution=(2160, 1620)))  #"最初に戻る"
        time.sleep(3)
        touch((955, 445))  #"写真"を開く
        time.sleep(3)
        touch(Template(r"tpl1687917094150.png", record_pos=(-0.099, 0.202), resolution=(2160, 1620)))  #"いいね"
        time.sleep(3)
        touch(Template(r"tpl1687917133945.png", record_pos=(-0.098, 0.202), resolution=(2160, 1620)))  #"いいね"を
        time.sleep(3)
        touch(Template(r"tpl1685072611131.png", record_pos=(0.436, -0.281), resolution=(2160, 1620)))  #"売場の写真"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1685072650256.png", record_pos=(0.051, -0.275), resolution=(2160, 1620)))  #"自店の写真"画面を開く
        time.sleep(3)
        touch(Template(r"tpl1685327432185.png", record_pos=(-0.063, -0.274), resolution=(2160, 1620)))  #"みんなの写真"画面に戻る
        time.sleep(3)
        touch(Template(r"tpl1685072706019.png", record_pos=(0.431, -0.28), resolution=(2160, 1620)))  #トップメニューに戻る
        time.sleep(3)
        touch(Template(r"tpl1685072778698.png", record_pos=(0.417, 0.178), resolution=(2160, 1620)))  #"チャンスロス"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1690787581098.png", record_pos=(0.284, -0.278), resolution=(2160, 1620)))  #"前日"をクリック
        time.sleep(3)
        touch(Template(r"tpl1690787616338.png", record_pos=(0.36, -0.277), resolution=(2160, 1620)))  #"翌日"をクリック
        time.sleep(3)
        touch(Template(r"tpl1685072830392.png", record_pos=(0.433, -0.281), resolution=(2160, 1620)))  #トップメニューに戻る
        time.sleep(3)
        touch(Template(r"tpl1690789352094.png", record_pos=(0.469, -0.346), resolution=(2160, 1620)))  #"設定メニュー"を開く
        time.sleep(3)
        touch(Template(r"tpl1690789393234.png", record_pos=(0.351, -0.243), resolution=(2160, 1620)))  #"マイクの設定"を開く
        time.sleep(3)
        touch((839, 1042))  #マイクの数字0になる
        time.sleep(3)
        touch((1023, 1042))  #マイクの数字50になる
        time.sleep(3)
        touch(Template(r"tpl1690791494305.png", record_pos=(0.44, -0.276), resolution=(2160, 1620)))  #"トップメニュー"に戻る
        time.sleep(3)
        touch(Template(r"tpl1690789352094.png", record_pos=(0.469, -0.346), resolution=(2160, 1620)))  #"設定メニュー"を開く
        time.sleep(3)
        touch(Template(r"tpl1690791793046.png", record_pos=(0.343, -0.138), resolution=(2160, 1620)))  #"お問い合わせ”をクリック
        time.sleep(3)
        touch(Template(r"tpl1690791866211.png", record_pos=(0.441, -0.275), resolution=(2160, 1620)))  #"トップメニュー"に戻る
        time.sleep(3)
        # touch(Template(r"tpl1690789352094.png", record_pos=(0.469, -0.346), resolution=(2160, 1620)))  #"設定メニュー"を開く
        # time.sleep(3)
        # touch(Template(r"tpl1690792109931.png", record_pos=(0.37, -0.1), resolution=(2160, 1620)))  #"プライバシーポリシー"をクリック
        # time.sleep(3)
        # touch(Template(r"tpl1690792214281.png", record_pos=(-0.471, -0.356), resolution=(2160, 1620)))  #"トップメニュー"に戻る
        # time.sleep(3)
        touch(Template(r"tpl1685340943532.png", record_pos=(-0.471, -0.344), resolution=(2160, 1620)))  #"キーボード"ボタンをクリックする
        time.sleep(3)
        touch(Template(r"tpl1685340995489.png", record_pos=(-0.291, -0.346), resolution=(2160, 1620)))  #"キーボード"を開く
        time.sleep(3)
        text("こんにちは")  #"こんにちは"を入力
        time.sleep(3)
        touch(Template(r"tpl1685341117668.png", record_pos=(-0.471, -0.344), resolution=(2160, 1620)))  #もう一度"キーボード"ボタンをクリックする
        time.sleep(3)
        stop_app("jp.co.couger.ludens")
        time.sleep(3)
finally:
    dev.stop_recording()
    simple_report(__file__, logpath=True)
