from PIL import Image

otkritki = {
    "8": "8m.jpg", # 8 марта
    "23": "23f.jpg", # 23 февраля
    "нг": "ng.jpg",
    "др": "dr.jpg",
}

prazdnik = input("К какому празднику нужна открытка? (8, 23, нг, др): ")

if prazdnik in otkritki:
    img = Image.open(otkritki[prazdnik])
    img.show()
else:
    print("Открытки к такому празднику нет!")