import qrcode

qr = qrcode.QRCode(
	version = 3,
	box_size = 15,
	border = 3
	)

data = 'URL'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill= 'black', back_color= 'white')
img.save('NAME')