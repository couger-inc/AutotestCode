import os
import shutil
import datetime

# このスクリプトは、"C:\FluxPdfFile" フォルダ内の "MN", "NP", "WP" サブフォルダにある
# "xx_01_20250224.pdf" というファイルを元に以下の手順を実行します:
# 1) ファイルを 16 個 (01~16) に増やして日付はそのまま (20250224)。
# 2) 2025年2月24日を除いたその後の月曜日の日付ごとに、同じく 16 個ずつファイルをコピー・リネームする。
#    (最後の月曜日は 2025年12月29日)

# ---基本設定---
base_dir = r"C:\FluxPdfFile"  # 親フォルダのパス
subfolders = ["MN", "NP", "WP"]  # 対象となるサブフォルダ
base_date_str = "20250224"  # 元となる日付 (YYYYMMDD)
original_index = "01"  # 元のファイル名にあるインデックス (01)

# ---日付関連の処理---
# まず 2025-02-24 (除外する日) の翌週月曜日から 2025年の最後の月曜日 (12/29) までを取得する
start_date = datetime.date(2025, 2, 24)
end_date = datetime.date(2025, 12, 31)

# (1) 2/24 が月曜日なので、次の月曜日は 3/3 から開始
# (2) 12/29 まで取り出す

mondays_after_224 = []
current_date = start_date + datetime.timedelta(days=7)  # 2/24 の翌週 -> 3/3
while current_date <= end_date:
    if current_date.weekday() == 0:  # 0: 月曜日
        mondays_after_224.append(current_date)
    current_date += datetime.timedelta(days=1)


# ---ファイルをコピーする処理---
def copy_and_rename_files(folder_name: str):
    """
    指定されたサブフォルダ内の "XX_01_20250224.pdf" を元に、
    1) インデックス(01->02~16)を変えて 16 ファイル作成
    2) さらに上記の月曜日の数だけ日付部分を変えてコピーする
    """
    # サブフォルダのパス
    folder_path = os.path.join(base_dir, folder_name)

    # 元ファイル名 (例: "MN_01_20250224.pdf")
    original_filename = f"{folder_name}_{original_index}_{base_date_str}.pdf"
    original_file_path = os.path.join(folder_path, original_filename)

    # まず 01 -> 02~16 のファイルを作成（同じ日付 20250224）
    # 既に存在する場合は上書きまたはスキップの判断が必要だが、今回は単純に上書きと仮定
    for i in range(2, 17):  # 2から16
        new_index_str = str(i).zfill(2)  # 2桁ゼロ埋め
        new_filename = f"{folder_name}_{new_index_str}_{base_date_str}.pdf"
        new_file_path = os.path.join(folder_path, new_filename)

        # ファイルコピー
        shutil.copy2(original_file_path, new_file_path)
        # copy2を使うとメタデータ（作成日時など）もコピーされます

    # 次に、取得した月曜日ごとに、上で作成した 16 ファイルを日付置換してコピー
    # つまり "xx_01_YYYYMMDD.pdf" ~ "xx_16_YYYYMMDD.pdf" を、各月曜日の日付で再作成
    for monday_date in mondays_after_224:
        # YYYYMMDD 形式の文字列に変換
        monday_date_str = monday_date.strftime("%Y%m%d")

        # 元になる 16 個のファイル(このサブフォルダ、日付=20250224、インデックス=01~16) を参照
        for i in range(1, 17):
            index_str = str(i).zfill(2)

            # 元ファイルのパス(コピー元)
            source_filename = f"{folder_name}_{index_str}_{base_date_str}.pdf"
            source_file_path = os.path.join(folder_path, source_filename)

            # 新しいファイルのパス(コピー先) 日付部分を monday_date_str に置換
            dest_filename = f"{folder_name}_{index_str}_{monday_date_str}.pdf"
            dest_file_path = os.path.join(folder_path, dest_filename)

            shutil.copy2(source_file_path, dest_file_path)


# ---メイン処理---
def main():
    # MN, NP, WP 各フォルダに対してファイルコピー・リネームを実行
    for sub in subfolders:
        copy_and_rename_files(sub)


if __name__ == "__main__":
    main()
