from PIL import Image

img = Image.open("10.1.png")

obrez = img.crop((100, 100, 305, 400))
obrez.save("obrez1.jpg")
obrez.show()