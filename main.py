import PySimpleGUI as sg

sg.theme('Default')

layout = [[sg.Button("CLICK")],]

window = sg.Window('Mi ventana', layout, size=(1920,1080))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()


