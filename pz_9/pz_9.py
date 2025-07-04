# Организовать словарь на 10 русско-английских слов, обеспечивающий
# "перевод" русского слова на английский.

rus_eng = { "окно": "window",
    "дверь": "door",
    "шкаф": "closet",
    "диван": "sofa",
    "цветок": "flower",
    "мужчина": "man",
    "женщина": "woman",
    "чай": "tea",
    "стол": "table",
    "мяч": "ball" }

translate = input("Введите слово на русском языке: ")
translation = rus_eng.get(translate)
if translation is not None:
  print("Перевод: ", rus_eng[translate])
else:
  print("Этого слова нет в словаре.")