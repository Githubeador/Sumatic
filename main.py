import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [[sg.Text("PULSA AQUÍ")]]

windows = sg.Window("Sumatic", layout, size=(1920,1080))

while True:
    event, values = windows.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "PULSA AQUÍ":
        sg.Popup("HOLA")

windows.close()
#

