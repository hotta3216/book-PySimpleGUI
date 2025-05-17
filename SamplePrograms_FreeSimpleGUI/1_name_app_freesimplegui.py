# 1_name_app_freesimplegui.py
import FreeSimpleGUI as sg

layout = [
    [sg.Text('名前を入力してください')],
    [sg.Input()],
    [sg.Button('Submit')],
    ]

window = sg.Window('名前入力アプリ', layout)

while True:
    event, values = window.read()
    print(event)
    if event == 'Submit':
        sg.popup(f'あなたの名前は {values[0]} です', title='結果')
    if event == None or event == 'Cancel':
        break

window.close()