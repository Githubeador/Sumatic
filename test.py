import PySimpleGUI as sg

sg.theme("DarkAmber")

layout1 = [[sg.Button("PULSA AQUÍ")]]

windows = sg.Window("Sumatic", layout, size=(1920,1080))

layout2 =

windows =

while True:
    event, values = windows.read()
    if event == sg.WIN_CLOSED:
        break

windows.close()



