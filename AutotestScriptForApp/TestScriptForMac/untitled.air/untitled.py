# -*- encoding=utf8 -*-
__author__ = "xushe"

from airtest.core.api import *

auto_setup(__file__)



dev = device()
dev.start_recording(output="test.mp4", max_time="36000")

try:
    for times in range(10):
        touch(Template(r"tpl1727219750141.png", record_pos=(-0.42, -0.318), resolution=(2160, 1620)))

        text("日本のおいしいものを10個教えて",enter=False)
        time.sleep(2)
        touch(Template(r"tpl1727219795159.png", record_pos=(0.424, 0.173), resolution=(2160, 1620)))
        time.sleep(5)
        touch(Template(r"tpl1727219750141.png", record_pos=(-0.42, -0.318), resolution=(2160, 1620)))

        text("ありがとう",enter=False)
        time.sleep(2)
        touch(Template(r"tpl1727219795159.png", record_pos=(0.424, 0.173), resolution=(2160, 1620)))
        time.sleep(2)


finally:
    dev.stop_recording()