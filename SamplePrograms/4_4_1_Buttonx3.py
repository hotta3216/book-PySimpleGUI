# 4_4_1_Buttonx3.py
import PySimpleGUI as sg

# 部品を定義し、配置順で2次元リストを作成
layout = [
    [sg.Button('グー'), sg.Button('チョキ'), sg.Button('パー'), ],
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

    # ボタンをクリックしたときのイベントを表示
    sg.popup(f'あなたは {event} を出しました')

window.close()