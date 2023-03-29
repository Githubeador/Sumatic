import PySimpleGUI as sg

sg.theme("DarkTeal4")

layout1 = [[sg.Button("atrás"), sg.Button("siguiente")]]

window1 = sg.Window("SUMATIC", layout1)

while True:
    event, values = window1.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == sg.Button#seguir escriviendo <---
window1.close()