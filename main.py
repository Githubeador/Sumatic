import PySimpleGUI as sg
from PIL import Image

sg.theme('Default')

layout = [[sg.Button("CLICK")], [sg.Image("fondo_montanas.png")]]


window = sg.Window('Mi ventana', layout, size=(1920,1080))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()


