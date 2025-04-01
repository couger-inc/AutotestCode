# -*- encoding=utf8 -*-
__author__ = "joseishou"

from airtest.core.api import *
from airtest.report.report import simple_report


auto_setup(__file__,logdir=True,devices=["ios:///127.0.0.1:8100"])

dev = device()
dev.start_recording(output="test.mp4", max_time="36000", orientation=2)

try:
    start_app("jp.co.couger.ludens")   #アプリ起動する
    time.sleep(10)

    text("12qwaszx!",enter = False)  #パスワード入力する
    time.sleep(3)

    touch(Template(r"tpl1684723341307.png", record_pos=(0.001, -0.106), resolution=(2160, 1620)))   #"OK"ボタンをクリックする
    time.sleep(10)

    if exists(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620))):  #ダイアログ判断
        touch(Template(r"tpl1703048273995.png", record_pos=(-0.069, 0.243), resolution=(2160, 1620)))   #画面転移キャンセル
        time.sleep(2)

    for times in range(100):

        touch(Template(r"tpl1709628911858.png", record_pos=(0.281, -0.092), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629246393.png", record_pos=(0.415, -0.141), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629274856.png", record_pos=(-0.053, -0.273), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629290200.png", record_pos=(0.415, -0.142), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629304441.png", record_pos=(0.097, -0.275), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709630874744.png", record_pos=(0.312, -0.093), resolution=(2160, 1620)))

        time.sleep(3)
        touch(Template(r"tpl1709629343841.png", record_pos=(0.434, -0.281), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709628911858.png", record_pos=(0.281, -0.092), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629449841.png", record_pos=(0.416, -0.141), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629274856.png", record_pos=(-0.053, -0.273), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629483975.png", record_pos=(0.416, -0.194), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629304441.png", record_pos=(0.097, -0.275), resolution=(2160, 1620)))
        time.sleep(3)
        swipe((0.57,0.981),(0.57,0.233))
        time.sleep(3)
        swipe((0.57,0.981),(0.57,0.233))
        time.sleep(3)
        touch(Template(r"tpl1709629525208.png", record_pos=(0.313, -0.103), resolution=(2160, 1620)))
        time.sleep(3)
        touch(Template(r"tpl1709629343841.png", record_pos=(0.434, -0.281), resolution=(2160, 1620)))
        time.sleep(3)
finally:
    dev.stop_recording()
    simple_report(__file__, logpath=True)