# -*- coding: utf-8 -*-
from airtest.core.api import *
import wda

# AirtestでWDAに接続（デバイスが正しくバインドされていることを確認する）
auto_setup(__file__, logdir=True, devices=["ios:///http://127.0.0.1:8100?cap_method=direct"])

# WDAに直接接続
client = wda.Client("http://127.0.0.1:8100")

# WDAへの接続が成功していることを確認する
if client.status().get("state") == "success":
    print("✅ WDAへの接続に成功しました！")
else:
    raise RuntimeError("❌ WDAへの接続に失敗しました。WDAが正しく動作しているか確認してください")

# WDAを使用してアプリを起動（start_app() の代わり）
client.app_launch("jp.co.couger.ludens")
time.sleep(5)

print(233)