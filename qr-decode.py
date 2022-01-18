import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr = pyqrcode.create("HORN O.K. PLEASE.")
qr.png("horn.png", scale=6)
a = decode(Image.open('ctie.jpg'))
print(a[0].data)

