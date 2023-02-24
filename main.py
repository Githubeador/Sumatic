import PySimpleGUI as sg

layout = [[sg.Text('Presione uno de los botones:')],
          [sg.Button('Botón 1', key='boton1'), sg.Button('Botón 2', key='boton2')]]

window = sg.Window('Ejemplo de botones', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'boton1':
        print('Ha presionado el botón 1')
    elif event == 'boton2':
        print('Ha presionado el botón 2')

window.close()
#

