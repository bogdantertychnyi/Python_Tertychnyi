magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
domknigi = {"Толстой","Грибоедов","Чехов","Пушкин"}
bookmarket ={"Пушкин", "Достоевский", "Маяковский"}
galery = {"Чехов","Тютчев","Пушкин"}

shops = set()

if "Пушкин" and "Тютчев" in magistr:
    shops.add("Магистр")
if "Пушкин" and "Тютчев" in domknigi:
    shops.add("ДомКниги")
if "Пушкин" and "Тютчев" in bookmarket:
    shops.add("БукМаркет")
if "Пушкин" and "Тютчев" in galery:
    shops.add("Галерея")

print("Магазины, в которых есть книги Пушкина и Тютчева:", shops)
