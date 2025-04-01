# -*- coding: utf-8 -*-
from airtest.core.api import *
import wda

# 让 Airtest 连接 WDA（确保设备正确绑定）
auto_setup(__file__, logdir=True, devices=["ios:///http://127.0.0.1:8100?cap_method=direct"])

# 直接连接 WDA
client = wda.Client("http://127.0.0.1:8100")

# 确保 WDA 连接成功
if client.status().get("state") == "success":
    print("✅ WDA 已成功连接！")
else:
    raise RuntimeError("❌ WDA 连接失败，请检查 WDA 是否正确运行")

# 使用 WDA 启动应用（替代 start_app()）
client.app_launch("jp.co.couger.ludens")
print("✅ 应用 jp.co.couger.ludens 已成功启动！")
time.sleep(5)
# 进行 UI 交互（Airtest 仍然可用）
touch(Template("1.png"))  # 确保 1.png 在正确的路径下