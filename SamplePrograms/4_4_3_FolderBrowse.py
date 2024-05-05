# 4_4_3_FolderBrowse.py
import PySimpleGUI as sg

# 部品を定義し、配置順で2次元リストを作成
layout = [
    [sg.Input(), sg.FolderBrowse()],
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