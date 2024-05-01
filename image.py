import PySimpleGUIQt as sg

# Define the layout
layout = [
    [sg.Text('Image Display Example')],
    [sg.Image(filename='Filename.jpg')],
    [sg.Button('Close')]
]

# Create the window
window = sg.Window('Image Display', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break

# Close the window
window.close()
