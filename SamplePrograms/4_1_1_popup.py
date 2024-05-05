# 4_1_1_popup.py
import PySimpleGUI as sg

value = sg.popup('OKボタンのみの\nポップアップウィンドウ', title='popup')

sg.popup(value) # popupの戻り値を表示
