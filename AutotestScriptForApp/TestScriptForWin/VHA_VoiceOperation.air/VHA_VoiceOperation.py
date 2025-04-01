#!C:\Python\Python312\python.exe
# -*- encoding=utf8 -*-

__author__ = "徐"

import pandas as pd
import datetime
import json
import logging
import shutil
import sys
from airtest.core.api import *
from airtest.report.report import LogToHtml
from colorama import Fore, Style, init

init(autoreset=True)


def load_config():
    """設定ファイルを読み込む"""
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)  # 設定ファイルconfig.jsonを開き、JSONデータとして読み込む


def get_current_time_for_filename():
    """ファイル名に使用される現在の時刻文字列を取得します"""
    return datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")


def get_current_time_for_print():
    """操作ステップの印刷に使用される現在の時刻文字列を取得します"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def setup_logging(log_directory, log_level):
    for logger_name in logging.root.manager.loggerDict:
        logging.getLogger(logger_name).setLevel(getattr(logging, log_level))
    """ログ設定を行う"""
    current_time = get_current_time_for_filename()
    local_logger = logging.getLogger(__name__)
    local_logger.setLevel(log_level)  # config.jsonで指定されたログ レベルを使用します。
    log_file = os.path.join(log_directory, f"error_{current_time}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)  # ファイル ハンドラーも同じログ レベルを使用します
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    local_logger.addHandler(file_handler)
    return local_logger


def ensure_directory_exists(directory):
    """ディレクトリが存在しない場合に作成する"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        custom_print(f"ディレクトリを作成しました: {directory}", color=Fore.LIGHTBLUE_EX, show_step=False, update_step=False)


class Counter:
    def __init__(self):
        self.step_counter = 1

    def increment_step(self):
        self.step_counter += 1
        return self.step_counter

    def reset_step(self):
        """歩数カウンターを初期値にリセット"""
        self.step_counter = 1


# ここでカウンターを初期化します
counter = Counter()


def custom_print(message, color=None, delay=0, update_step=True, show_step=True):
    """カスタムフォーマットでメッセージを出力する"""
    current_time = get_current_time_for_print()
    if show_step:
        output = f"[{current_time}] {counter.step_counter}: {message}"
    else:
        output = f"[{current_time}] {message}"
    if color:
        output = f"{color}{output}{Style.RESET_ALL}"
    print(output)
    if delay > 0:
        time.sleep(delay)
    if update_step:
        counter.increment_step()


def handle_action_result(action_result, action_target, stop_if_not_found, delay, logger):
    """アクションの結果を処理する"""
    if action_result is False and stop_if_not_found:
        error_message = f"対象が見つかりません: {action_target}"
        custom_print(error_message, color=Fore.RED, update_step=False)
        logger.error(error_message)
        raise ValueError(error_message)
    if delay > 0:
        time.sleep(delay)


def format_json_line_by_line(file_path):
    formatted_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                json_object = json.loads(line)
                formatted_line = json.dumps(json_object, indent=4, ensure_ascii=False)
                formatted_lines.append(formatted_line)
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in formatted_lines:
            file.write(line + "\n")
    custom_print('ログファイルは正常にフォーマットされました', update_step=False, show_step=False, color=Fore.LIGHTBLUE_EX,
                 delay=2)


def perform_action(action_type, action_target, description, logger, stop_if_not_found=True, delay=0, update_step=True, use_rgb=False, **kwargs):
    """UIアクションを実行する"""
    action_funcs = {
        'wait': lambda: wait(Template(action_target, rgb=use_rgb), timeout=10, **kwargs),
        'swipe': lambda: swipe(kwargs['start_point'], kwargs['end_point'], **kwargs),
        'exists': lambda: exists(Template(action_target)),
        'touch': lambda: touch(Template(action_target), **kwargs),
        'start_app': lambda: start_app(action_target),
        'text': lambda: text(action_target, **kwargs),
        'snapshot': lambda: snapshot(**kwargs),
        'double_touch': lambda: double_click(Template(action_target)),
        'key_press': lambda: keyevent(kwargs['key']),
        'assert_exists': lambda: assert_exists(Template(action_target), description),
        'stop_app': lambda: stop_app(action_target)
    }

    try:
        # アクションの種類に応じて、適切なアクション関数を選択して実行します
        if "検出中：" in description:
            color = Fore.LIGHTGREEN_EX
        elif "入力:" in description:
            color = Fore.LIGHTBLUE_EX
        else:
            color = Fore.LIGHTYELLOW_EX

        custom_print(description, color=color, update_step=update_step)
        result = action_funcs[action_type]()
        handle_action_result(result, action_target, stop_if_not_found, delay, logger)
        return result
    except KeyError:
        error_message = f"サポートされていないaction_type: {action_type}"
        custom_print(error_message, color=Fore.RED, update_step=False)
        logger.error(error_message)
        raise NotImplementedError(error_message)
    except Exception as e:
        error_message = f"アクション {action_type} 実行中にエラーが発生しました、対象：{action_target}、エラー：{str(e)}"
        custom_print(error_message, color=Fore.RED, update_step=False)
        logger.error(error_message)
        sys.exit(1)


def generate_video_filename():
    """ビデオファイル名を生成する"""
    current_file_name = os.path.splitext(os.path.basename(__file__))[0]
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{current_file_name}_{current_time}.mp4"


def generate_report(script_root, log_root, export_dir, logfile):
    """ログからHTMLレポートを生成する"""
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    export_dir = os.path.join(export_dir, f"report_{current_time}")

    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
    html_reporter = LogToHtml(script_root=script_root, log_root=log_root, export_dir=export_dir, logfile=logfile,
                              lang='en')
    html_reporter.report()


def load_excel_data(file_path):
    """Excelファイルを読み込む"""
    return pd.read_excel(file_path)


def main():
    """メイン関数、自動化スクリプトを実行する"""
    config = load_config()
    platform_config = config['windows'] if sys.platform.startswith('win') else config['mac']
    log_directory_airtest = platform_config['log_root']
    log_level = platform_config['log_level']  # config.jsonからログレベルを取得する

    if os.path.exists(log_directory_airtest):
        shutil.rmtree(log_directory_airtest)
        custom_print(f"ログフォルダが削除されました: {log_directory_airtest}", color=Fore.LIGHTBLUE_EX, show_step=False, update_step=False)

    excel_data = load_excel_data('VHA_VoiceOperation.xlsx')   # Excelファイルを読み込む

    auto_setup(__file__, logdir=True, devices=[platform_config['device_connection_string']])
    dev = device()
    video_filename = generate_video_filename()
    dev.start_recording(output=video_filename, max_time=36000, orientation=2)
    custom_print('録画開始', update_step=False, show_step=False, color=Fore.LIGHTBLUE_EX, delay=2)
    ensure_directory_exists(platform_config['export_dir'])
    logger = setup_logging(log_directory_airtest, log_level)  # log_level と timestamp_format がここに渡されていることを確認

    try:
        counter.reset_step()  # 歩数カウンターをリセット

        # perform_action("start_app", "jp.co.couger.ludens", "アプリ起動", logger, delay=15)
        #
        # perform_action("wait", "1.png", "検出中：起動成功したかを確認中", logger, delay=3)
        #
        # perform_action("text", "12qwaszx!", "起動成功、パスワードを入力する", logger, enter=False, delay=3)
        #
        # perform_action("touch", "1.png", "OKボタンをタップする", logger, delay=3)
        #
        # perform_action("wait", "2.png", "検出中：ログインの状態を確認中", logger, delay=3)
        #
        # custom_print('ログイン成功、レイチェルの発話終わるのを待ち', update_step=True, color=Fore.LIGHTYELLOW_EX, delay=10)
        #
        # if perform_action("exists", "3.png", "検出中：画面上に画面遷移ダイアログが表示されているかを確認中", logger,
        #                   stop_if_not_found=False):
        #     perform_action("touch", "3.png", "画面遷移ダイアログが検出されたので、「いいえ」をタップする", logger,
        #                    delay=3)
        # else:
        #     custom_print('目標見つかりません、次のステップを続く', update_step=True, color=Fore.LIGHTRED_EX, delay=3)
        #
        # perform_action("touch", "4.png", "キーボードボタンをタップする", logger, delay=3)

        for index, row in excel_data.iterrows():
            text_to_enter = row['A']  # Excelデータからテキストを取得する
            perform_action("touch", "6.png", "キーボードを開く", logger, delay=3)
            perform_action("text", text_to_enter, f"入力: {text_to_enter}", logger, enter=False, delay=3)
            perform_action("touch", "7.png", "「Enter」ボタンをタップする", logger, delay=3)
            perform_action("touch", "5.png", "「X」ボタンをタップする", logger, delay=3)

        # perform_action("stop_app", "jp.co.couger.ludens", "アプリ閉じる", logger, delay=3)

    except Exception as exc:
        print(f"スクリプトエラー: {str(exc)}")
        sys.exit(1)
    finally:
        dev.stop_recording()
        custom_print('録画終了', update_step=False, show_step=False, color=Fore.LIGHTBLUE_EX, delay=2)
        generate_report(platform_config['script_root'], platform_config['log_root'], platform_config['export_dir'], platform_config['logfile'])
        format_json_line_by_line(platform_config['logfile'])


if __name__ == "__main__":
    main()