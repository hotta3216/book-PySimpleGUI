# 5_2_2_Input_clear.py
import FreeSimpleGUI as sg

# 部品を定義し、配置順で2次元リストを作成
layout = [
    [sg.Input(key='input')],
    [sg.Button('Submit'), sg.Button('Clear')],
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

    # Clearボタンをクリックしたらテキスト入力フィールドを消去
    if event == 'Clear':
        window['input'].update('')

    # Submitをクリックしたら結果を表示
    if event == 'Submit':
        sg.popup(values)

window.close()