import PySimpleGUIQt as s
import image as img

def get_input_text():
    thelayout = [
        [s.Text('Qr Code Generator!', size=(60, 1), font=("Helvetica", 20), justification='center')],
        [s.Text('Welcome Fella! Enjoy the Qr Code Generator!', size=(60, 1), font=("Helvetica", 15), justification='center')],
        [s.InputText('Filename', key='filename')],  # Added key to the InputText widget
        [s.Multiline('This is my text', key='input_text')],  # Added key to the Multiline widget
        [s.Submit('Submit'), s.Cancel()]  # Changed the button text
    ]

    window = s.Window(title="Qr Code Generator!", size=(640,480), layout=thelayout)
    button, values = window.read()

    if button == 'Submit':  # Check if the Submit button was clicked
        file_name_value = values['filename']  # Get the value from the InputText widget
        input_text_value = values['input_text']  # Get the value from the InputText widget
        window.close()
        return file_name_value, input_text_value
    else:
        window.close()
        return None, None
