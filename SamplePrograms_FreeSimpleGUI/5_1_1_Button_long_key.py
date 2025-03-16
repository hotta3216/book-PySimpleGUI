# 5_1_1_Button_long_key.py
import FreeSimpleGUI as sg

# 部品を定義し、配置順で2次元リストを作成
layout = [
    [sg.Text('小野小町が詠んだ歌はどれ？')],
    [sg.Button('めぐりあひて 見しやそれともわかぬまに 雲隠れにし夜はの月かな', key=1)],
    [sg.Button('花の色は うつりにけりないたづらに わが身世にふるながめせしまに', key=2)],
    [sg.Button('夜をこめて とりのそらねははかるとも よに逢坂の関は許さじ', key=3)],
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

    if event == 2:
        sg.popup('おめでとう！正解です！')
    else:
        sg.popup('残念！不正解です！')

window.close()