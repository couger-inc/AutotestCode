# -*- encoding=utf8 -*-
__author__ = "shengqing"

from airtest.core.api import *

auto_setup(__file__)

# ケース-2
touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
time.sleep(10)
touch(Template(r"tpl1683705874104.png", record_pos=(0.462, 0.337), resolution=(2160, 1620)))
time.sleep(3)
touch(Template(r"tpl1683706909580.png", record_pos=(-0.104, 0.176), resolution=(2160, 1620)))
time.sleep(3)
swipe(Template(r"tpl1683598546213.png", record_pos=(0.31, -0.169), resolution=(2160, 1620)), vector=[0.0016, -0.2862])
touch(Template(r"tpl1683707098462.png", record_pos=(-0.251, -0.087), resolution=(2160, 1620)))
time.sleep(5)

# ケース-4
touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
time.sleep(3)
keyevent("HOME")
time.sleep(10)
touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
time.sleep(5)
touch(Template(r"tpl1683705874104.png", record_pos=(0.462, 0.337), resolution=(2160, 1620)))
time.sleep(3)
touch(Template(r"tpl1683706909580.png", record_pos=(-0.104, 0.176), resolution=(2160, 1620)))
time.sleep(3)
swipe(Template(r"tpl1683598546213.png", record_pos=(0.31, -0.169), resolution=(2160, 1620)), vector=[0.0016, -0.2862])
touch(Template(r"tpl1683707098462.png", record_pos=(-0.251, -0.087), resolution=(2160, 1620)))
time.sleep(5)


# ケース-6
touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
time.sleep(8)
keyevent("HOME")
time.sleep(10)
touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
time.sleep(5)
touch(Template(r"tpl1683705874104.png", record_pos=(0.462, 0.337), resolution=(2160, 1620)))
time.sleep(3)
touch(Template(r"tpl1683706909580.png", record_pos=(-0.104, 0.176), resolution=(2160, 1620)))
time.sleep(3)
swipe(Template(r"tpl1683598546213.png", record_pos=(0.31, -0.169), resolution=(2160, 1620)), vector=[0.0016, -0.2862])
touch(Template(r"tpl1683707098462.png", record_pos=(-0.251, -0.087), resolution=(2160, 1620)))
time.sleep(3)

#　ケース-7
touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
time.sleep(8)
touch(Template(r"tpl1683861144641.png", record_pos=(0.459, 0.118), resolution=(2160, 1620)))
time.sleep(1)
touch(Template(r"tpl1683857813629.png", record_pos=(-0.001, 0.239), resolution=(2160, 1620)))
time.sleep(3)
keyevent("HOME")
time.sleep(1)
keyevent("HOME")
time.sleep(3)

# ケース-9
touch(Template(r"tpl1683705874104.png", record_pos=(0.462, 0.337), resolution=(2160, 1620)))
time.sleep(1)
touch(Template(r"tpl1683706909580.png", record_pos=(-0.104, 0.176), resolution=(2160, 1620)))
time.sleep(3)
swipe(Template(r"tpl1683598546213.png", record_pos=(0.31, -0.169), resolution=(2160, 1620)), vector=[0.0016, -0.2862])
touch(Template(r"tpl1683707098462.png", record_pos=(-0.251, -0.087), resolution=(2160, 1620)))
time.sleep(3)
touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
time.sleep(3)
touch(Template(r"tpl1683705874104.png", record_pos=(0.462, 0.337), resolution=(2160, 1620)))
time.sleep(3)
touch(Template(r"tpl1683706909580.png", record_pos=(-0.104, 0.176), resolution=(2160, 1620)))
time.sleep(3)
swipe(Template(r"tpl1683598546213.png", record_pos=(0.31, -0.169), resolution=(2160, 1620)), vector=[0.0016, -0.2862])
touch(Template(r"tpl1683707098462.png", record_pos=(-0.251, -0.087), resolution=(2160, 1620)))
time.sleep(3)

# ケース-11
for t in range(10):
    touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
    time.sleep(5)
    touch(Template(r"tpl1683705874104.png", record_pos=(0.462, 0.337), resolution=(2160, 1620)))
    time.sleep(3)
    touch(Template(r"tpl1683706909580.png", record_pos=(-0.104, 0.176), resolution=(2160, 1620)))
    time.sleep(3)
    swipe(Template(r"tpl1683598546213.png", record_pos=(0.31, -0.169), resolution=(2160, 1620)), vector=[0.0016, -0.2862])
    touch(Template(r"tpl1683707098462.png", record_pos=(-0.251, -0.087), resolution=(2160, 1620)))
    time.sleep(3)
    
# ケース-13~16
    
touch(Template(r"tpl1683705732858.png", record_pos=(0.34, -0.047),))
time.sleep(10)
text("1234eszxcv!",enter=False)
time.sleep(2)
for t1 in range(11):
    text("\b",enter = False)
time.sleep(3)
text("12qwaszx!",enter = False)
time.sleep(2)
touch(Template(r"tpl1683879333053.png", record_pos=(-0.002, -0.108), resolution=(2160, 1620)))