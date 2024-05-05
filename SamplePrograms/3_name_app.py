# 3_name_app.py
# ライブラリをインポート
import PySimpleGUI as sg

# 部品を定義し、配置順で2次元リストを作成
layout = [
    [sg.Text('名前を入力してください')],
    [sg.Input()],
    [sg.Button('Submit'), sg.Button('Cancel')],
    ]

# ウィンドウを表示し部品を配置
window = sg.Window('名前入力アプリ', layout)

# イベント待ちのための無限ループ
while True:
    # ウィンドウ読み取り
    event, values = window.read()

    # Submitをクリックしたときの処理
    if event == 'Submit':
        sg.popup(f'あなたの名前は {values[0]} です', title='結果')

    # Cancelをクリックまたはウィンドウクローズ時はループを抜ける
    if event == None or event == 'Cancel':
        break

# 最後にウィンドウを閉じて終了
window.close()