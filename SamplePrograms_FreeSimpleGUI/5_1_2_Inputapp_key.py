# 5_1_2_Inputapp_key.py
import FreeSimpleGUI as sg

era_name = ['明治', '大正', '昭和', '平成', '令和']

# 部品を定義し、配置順で2次元リストを作成
layout = [
    [sg.Text('あなたの情報を入力してください')],
    [sg.Text('氏名'), sg.Input(key='name')],
    [
        sg.Text('性別'),
        sg.Radio('男', 'group1', key='male'),
        sg.Radio('女', 'group1', key='female'),
        sg.Radio('選択しない', 'group1', key='dns'),
    ],
    [
        sg.Text('生年月日'),
        sg.Combo(era_name, size=(5, 1), key='era'),
        sg.Combo(list(range(1, 65)), size=(3, 1), key='year'),
        sg.Text('年'),
        sg.Combo(list(range(1, 13)), size=(3, 1), key='month'),
        sg.Text('月'),
        sg.Combo(list(range(1, 32)), size=(3, 1), key='day'),
        sg.Text('日'),
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