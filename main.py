import PySimpleGUI as sg
import random
import re

# Generate a random challenge based on the selected operation
def generate_challenge(operation):
    challenge = ""
    answer = 0
    if operation == "sum":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        challenge = f"What is {a} + {b}?"
        answer = a + b
    elif operation == "subtract":
        a = random.randint(1, 10)
        b = random.randint(1, a)
        challenge = f"What is {a} - {b}?"
        answer = a - b
    elif operation == "multiply":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        challenge = f"What is {a} x {b}?"
        answer = a * b
    return challenge, answer

def replace_string(string):
    pattern = r"-([A-Z]+)-"
    matches = re.findall(pattern, string)
    for match in matches:
        replacement = match.lower()
        string = string.replace(f"-{match}-", replacement)
    return string

sg.theme("DarkTeal7")

# Start menu layout
start_menu_layout = [
    [sg.Button("JUGAR", key="-START-", size=(20, 2), pad=(300, 200))]
]

# Select operation layout
operation_layout = [
    [sg.Button("Sum", key="-SUM-", button_color=("white", "green"), size=(20, 2), pad=(300, 200))],
    [sg.Button("Subtract", key="-SUBTRACT-", button_color=("white", "red"), size=(20, 2), pad=(300, 0))],
    [sg.Button("Multiply", key="-MULTIPLY-", button_color=("white", "blue"), size=(20, 2), pad=(300, 0))],
    [sg.Button("Exit", size=(20, 2), pad=(300, 200))]
]

# Challenge layout
challenge_layout = [
    [sg.Text("Challenge:", font=("Helvetica", 14), key="-CHALLENGE-", pad=(0, 200))],
    [sg.InputText(key="-RESPONSE-", pad=(0, 0))],
    [sg.Button("Submit", size=(20, 2), pad=(0, 200))]
]

# Create the window
window = sg.Window("Math Challenge App", start_menu_layout, size=(1920, 1080))

# Event loop to process events and interact with the GUI
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "-START-":
        window.hide()
        start_window = sg.Window("Math Challenge App", operation_layout, finalize=True, size=(1920, 1080))
        start_window_event, start_window_values = start_window.read()
        if start_window_event == sg.WINDOW_CLOSED or start_window_event == "Exit":
            start_window.close()
            window.un_hide()
            continue
        operation = replace_string(start_window_event)  # Extract the selected operation from the event key
        challenge, answer = generate_challenge(operation)
        start_window.close()
        challenge_window = sg.Window("Math Challenge App", challenge_layout, finalize=True, size=(1920, 1080))
        challenge_window["-CHALLENGE-"].update(challenge)  # Update the challenge label
        close_challenge_window = False  # Flag to indicate when to close the challenge window

        while True:
            event, values = challenge_window.read()
            if event == sg.WINDOW_CLOSED or event == "Exit":
                close_challenge_window = True
                break
            elif event == "Submit":
                response = values["-RESPONSE-"]
                if response.isdigit():
                    response = int(response)
                    if response == answer:
                        sg.popup("Correct! Good job!")
                        challenge, answer = generate_challenge(operation)  # Generate a new challenge
                        challenge_window["-CHALLENGE-"].update(challenge)  # Update the challenge label with the new challenge
                    else:
                        sg.popup("Incorrect. Try again!")
                else:
                    sg.popup("Please enter a valid response.")

        challenge_window.close()
        window.un_hide()  # Show the start menu window again

        if close_challenge_window:
            break

# Close the window
window.close()
