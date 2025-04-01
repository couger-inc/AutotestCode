# -*- encoding=utf8 -*-
__author__ = "shengqing"

from airtest.core.api import *

auto_setup(__file__)
start_app("jp.co.couger.ludens")     #　アプリ起動
time.sleep(10)
text("12qwaszx!",enter = False)     #　アカウント入力
time.sleep(2)
touch(Template(r"tpl1688093014929.png", record_pos=(0.0, -0.107), resolution=(2160, 1620)))     # ログイン確認
time.sleep(15)
if exists(Template(r"tpl1688520868126.png", record_pos=(-0.107, 0.262), resolution=(2160, 1620))):
    touch(Template(r"tpl1688520868126.png", record_pos=(-0.107, 0.262), resolution=(2160, 1620)))  # 画面遷移キャンセル
    time.sleep(2)
for times in range(10):
    touch(Template(r"tpl1696408077458.png", record_pos=(0.305, 0.099), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1696410048504.png", record_pos=(0.432, -0.281), resolution=(2160, 1620)))
    time.sleep(2)
touch(Template(r"tpl1696408077458.png", record_pos=(0.305, 0.099), resolution=(2160, 1620)))
time.sleep(2)
keyevent("HOME")
time.sleep(10)
start_app("jp.co.couger.ludens")
for times1 in range(10):
    swipe(Template(r"tpl1696411102459.png", record_pos=(-0.025, 0.3), resolution=(2160, 1620)), vector=[-0.0112, -0.7396])
    time.sleep(2)
    swipe(Template(r"tpl1696411148714.png", record_pos=(-0.027, -0.202), resolution=(2160, 1620)), vector=[0.0152, 0.6735])
    time.sleep(2)
for times2 in range(10):
    touch(Template(r"tpl1696411662878.png", rgb=False, record_pos=(0.259, 0.146), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1696411733327.png", record_pos=(0.258, 0.144), resolution=(2160, 1620)))
    time.sleep(2)
for times3 in range(10):
    touch(Template(r"tpl1696411907695.png", record_pos=(0.344, 0.144), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1696411924389.png", record_pos=(0.345, 0.146), resolution=(2160, 1620)))
    time.sleep(2)
swipe(Template(r"tpl1696411102459.png", record_pos=(-0.025, 0.3), resolution=(2160, 1620)), vector=[-0.0112, -0.7396])
time.sleep(2)
for times4 in range(10):
    touch(Template(r"tpl1696411662878.png", rgb=False, record_pos=(0.259, 0.146), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1696411733327.png", record_pos=(0.258, 0.144), resolution=(2160, 1620)))
    time.sleep(2)
for times5 in range(10):
    touch(Template(r"tpl1696411907695.png", record_pos=(0.344, 0.144), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1696411924389.png", record_pos=(0.345, 0.146), resolution=(2160, 1620)))
    time.sleep(2)
for times6 in range(10):
    touch(Template(r"tpl1696412503948.png", record_pos=(0.376, 0.013), resolution=(2160, 1620)))
    time.sleep(2)
    touch(Template(r"tpl1696412522642.png", record_pos=(0.375, 0.013), resolution=(2160, 1620)))
    time.sleep(2)
stop_app("jp.co.couger.ludens")


