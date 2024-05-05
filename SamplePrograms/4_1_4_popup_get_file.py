# 4_1_4_popup_get_file.py
import PySimpleGUI as sg

value = sg.popup_get_file('ファイルを設定してください', title='ファイル選択')

sg.popup(value) # popup_get_fileの戻り値を表示