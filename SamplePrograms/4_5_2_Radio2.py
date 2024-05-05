# 4_5_2_Radio2.py
import PySimpleGUI as sg

# 部品を定義し、配置順で2次元リストを作成
layout = [
     # Radioの項目をリストで設定
    [
        sg.Radio('A', 'group1'),
        sg.Radio('B', 'group1'),
        sg.Radio('C', 'group1'),
    ],
    [
        sg.Radio('D', 'group2'),
        sg.Radio('E', 'group2'),
        sg.Radio('F', 'group2'),
    ],
    [sg.Button('Submit')],
    ]

# ウィンドウを表示し部品を配置
window = sg.Window('Title', layout)

# イベント待ちのための無限ループ
while True:
    # ウィンドウ読み取り
    event, values = window.read()

    # Submitをクリックしたときの処理
    if event == 'Submit':
        sg.popup(values)

    # ウィンドウクローズ時はループを抜ける
    if event == None:
        break

window.close()