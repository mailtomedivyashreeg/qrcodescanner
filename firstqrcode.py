import qrcode
img=qrcode.make("https://github.com/mailtomedivyashreeg")
img.save("qrcode.png")
print("created")