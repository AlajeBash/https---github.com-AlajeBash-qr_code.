import qrcode
import UI
import image as img
# Get input for the text and file name from the UI
filename, input_text = UI.get_input_text()

if filename is not None and input_text is not None:
    # Generate QR code
    qr = qrcode.make(input_text)

    # Save QR code as image
    qr.save(filename + '.jpg')

    print(f"Input Text: {input_text}")
    print(f"File Name: {filename}")
else:
    print("No input provided. Exiting...")

img()