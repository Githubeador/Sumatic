import PySimpleGUI as sg
import random, threading, re, playsound, os
import pygame

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)

def play_audio_player():
    audio_file = 'musica.mp3'
    play_audio(audio_file)

def generate_challenge(operation):
    challenge = ""
    answer = 0
    if operation == "sum":
        a = random.randint(1, 200)
        b = random.randint(1, 200)
        challenge = f"¿Cuánto es {a} + {b}?"
        answer = a + b
    elif operation == "subtract":
        a = random.randint(1, 100)
        b = random.randint(1, a)
        challenge = f"¿Cuánto es {a} - {b}?"
        answer = a - b
    elif operation == "multiply":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        challenge = f"¿Cuánto es {a} x {b}?"
        answer = a * b
    return challenge, answer

def replace_string(string):
    pattern = r"-([A-Z]+)-"
    matches = re.findall(pattern, string)
    for match in matches:
        replacement = match.lower()
        string = string.replace(f"-{match}-", replacement)
    return string

sg.theme("Tan")

start_menu_layout = [
    [sg.Button("JUGAR", key="-START-", size=(20, 4), pad=(300, 200))]
]

operation_layout = [
    [sg.Button("Sumas", key="-SUM-", button_color=("white", "green"), size=(20, 2), pad=((200, 200), (200, 20)))],
    [sg.Button("Restas", key="-SUBTRACT-", button_color=("white", "red"), size=(20, 2), pad=((200, 200), (0, 20)))],
    [sg.Button("Multiplicaciones", key="-MULTIPLY-", button_color=("white", "blue"), size=(20, 2), pad=((200, 200), (0, 20)))],
    [sg.Button("Salir", size=(20, 2), pad=((300, 200), (0, 200)))]
]

challenge_layout = [
    [sg.Text("Reto:", font=("Helvetica", 14), key="-CHALLENGE-", pad=(0, 200))],
    [sg.InputText(key="-RESPONSE-", pad=(0, 0))],
    [sg.Button("Enviar", size=(20, 2), pad=(0, 200))]
]

window = sg.Window("Ventana", start_menu_layout, size=(700, 500), element_justification='c')

counter = 0

while True:
    event, values = window.read()
    if counter == 0:
        play_audio_player()
        counter = 1

    if event == sg.WINDOW_CLOSED or event == "Salir":
        break
    elif event == "-START-":
        window.hide()
        start_window = sg.Window("Ventana", operation_layout, finalize=True, size=(700, 500), element_justification='c')
        start_window_event, start_window_values = start_window.read()
        if start_window_event == sg.WINDOW_CLOSED or start_window_event == "Salir":
            start_window.close()
            window.un_hide()
            continue
        operation = replace_string(start_window_event)
        challenge, answer = generate_challenge(operation)
        start_window.close()
        challenge_window = sg.Window("Ventana", challenge_layout, finalize=True, size=(800, 900), element_justification='c')
        challenge_window["-CHALLENGE-"].update(challenge)
        close_challenge_window = False

        while True:
            event, values = challenge_window.read()
            if event == sg.WINDOW_CLOSED or event == "Salir":
                close_challenge_window = True
                break
            elif event == "Enviar":
                response = values["-RESPONSE-"]
                if response.isdigit():
                    response = int(response)
                    if response == answer:
                        sg.popup("¡Correcto! ¡Buen Trabajo!")
                        challenge, answer = generate_challenge(operation)
                        challenge_window["-CHALLENGE-"].update(challenge)
                    else:
                        sg.popup("Incorrecto. ¡Inténtalo de nuevo!")
                else:
                    sg.popup("Por favor, ingresa una respuesta válida.")

        challenge_window.close()
        window.un_hide()

        if close_challenge_window:
            break

window.close()



