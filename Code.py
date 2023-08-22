# Importing library
import qrcode

# Data to encode
data = "Dhruvrajsinh Demo QR"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'blue',
					back_color = 'green')

img.save('QR_Code_Dhruvrajsinh_Rathod.png')
