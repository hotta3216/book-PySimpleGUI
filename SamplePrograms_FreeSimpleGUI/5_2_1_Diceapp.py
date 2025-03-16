# 5_2_1_Diceapp.py
import random
import FreeSimpleGUI as sg

# 部品を定義し、配置順で2次元リストを作成
layout = [
    [sg.Button('サイコロを振る')],
    [sg.Text('結果：', key='result')],
    ]

# ウィンドウを表示し部品を配置
window = sg.Window('title', layout)

# イベント待ちのための無限ループ
while True:
    # ウィンドウ読み取り
    event, values = window.read()

    # ウィンドウクローズ時はループを抜ける
    if event == None:
        break

    # サイコロを振って表示
    if event == 'サイコロを振る':
        roll = random.randint(1, 6)
        window['result'].update(f'結果： {roll}')

window.close()