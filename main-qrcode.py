import qrcode

text = input('Link or Text here\n')
qr = qrcode.make(text)
filename = input('Give your QrCode name: \n')
qr.save(filename+'.jpg')
