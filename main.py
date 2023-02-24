import PySimpleGUI as sg

sg.theme('LightBlue')

layout = [
    [sg.Image("fondo montañas.jpg"],
    [sg.Text('Hola, mundo!')]
]

window = sg.Window('Mi ventana', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()


