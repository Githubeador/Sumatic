import PySimpleGUI as sg

# Este script crea una ventana con un botón y la muestra en la pantalla
sg.theme('Default')

# Crear el diseño de la ventana
layout1 = [[sg.Button("CLICK")]]

# Crear la ventana
window1 = sg.Window('Mi ventana', layout1, size = (1920,1080))

# Bucle principal del programa
while True:
    # Leer los eventos de la ventana
    event, values = window1.read()

    # Si se produce el evento de cerrar la ventana, salir del bucle
    if event == sg.WIN_CLOSED:
        break

# Cerrar la ventana cuando el bucle principal termina
window1.close()

