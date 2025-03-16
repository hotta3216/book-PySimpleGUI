# 4_1_2_popup_yes_no.py
import FreeSimpleGUI as sg

value = sg.popup_yes_no('実行しますか？', title='確認')

sg.popup(value) # popup_yes_noの戻り値を表示
