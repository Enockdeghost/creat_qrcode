import qrcode

img = qrcode.make("http://github.com/Enockdeghost")
img.save('enock@github.jpg')