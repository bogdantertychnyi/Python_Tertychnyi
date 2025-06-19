# В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
# ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
# текстовый файл все даты февраля в формате ДД/ММ/ГГГГ

import re

# В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
# ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
# текстовый файл все даты февраля в формате ДД/ММ/ГГГГ

import re

file = open('dates.txt', 'r', encoding='utf-8')
content = file.read()

point = re.findall(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', content)
slash = re.findall(r'\b(\d{2})/(\d{2})/(\d{4})\b', content)

print(f'ДД.ММ.ГГГГ: {len(point)}')
print(f'ДД/ММ/ГГГГ: {len(slash)}')

slash_february = [f"{d[0]}/{d[1]}/{d[2]}" for d in slash if d[1] == '02']

filee = open('slash_february.txt', 'w', encoding='utf-8')
filee.write('\n'.join(map(str, slash_february)))
filee.close()
