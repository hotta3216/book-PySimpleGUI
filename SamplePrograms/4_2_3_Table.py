# 4_2_3_Table.py
import PySimpleGUI as sg

# テーブルのヘッダを定義
header = ['Name', 'Age', 'Gender', 'Favorite']
# テーブルのデータを定義
member_list = [
   ['Bob', 25, 'Male', 'りんご'],
   ['Tom', 32, 'Male', 'みかん'],
   ['Ivy', 23, 'Female', 'バナナ'],
]

# 部品を定義し、配置順で2次元リストを作成
layout = [
    [sg.Table(member_list, headings=header,
               justification='center')]
    ]

# ウィンドウを表示し部品を配置
window = sg.Window('Title', layout)

# イベント待ちのための無限ループ
while True:
    # ウィンドウ読み取り
    event, values = window.read()

    # ウィンドウクローズ時はループを抜ける
    if event == None:
        break

window.close()