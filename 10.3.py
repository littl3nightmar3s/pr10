from PIL import Image, ImageFont, ImageDraw

otkritki = {
    "8": "8m.jpg", # 8 марта
    "23": "23f.jpg", # 23 февраля
    "нг": "ng.jpg",
    "др": "dr.jpg",
}

prazdnik = input("К какому празднику нужна открытка? (8, 23, нг, др): ")
name = input("Введите имя того, кого хотите поздравить: ")

if prazdnik in otkritki:
    img = Image.open(otkritki[prazdnik])
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arialbd.ttf", 40)
    text = name + ", поздравляю!"
    draw.text((img.width // 2 - 100, 20), text, font=font, fill=(255, 0, 0))
    img.save("pozdravlenie.png")
    img.show()
else:
    print("Открытки к такому празднику нет")