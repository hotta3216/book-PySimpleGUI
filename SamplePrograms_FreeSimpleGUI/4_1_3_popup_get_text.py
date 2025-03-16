# 4_1_3_popup_get_text.py
import FreeSimpleGUI as sg

value = sg.popup_get_text('名前を入力してください', title='入力')

sg.popup(value) # popup_get_textの戻り値を表示