# В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
# ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
# текстовый файл все даты февраля в формате ДД/ММ/ГГГГ

import re

pattern_point = re.compile(r'\b(d{2}).(d{2}).(d{4})\b')
pattern_slash = re.compile(r'\b(d{2})/(d{2})/(d{4})\b')

file = open('dates.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

point = pattern_point.findall(content)
slash = pattern_slash.findall(content)

print(f'ДД.ММ.ГГГГ: {len(point)}')
print(f'ДД/ММ/ГГГГ: {len(slash)}')

slash_february = [f"{d[0]}/{d[1]}/{d[2]}" for d in slash if d[1] == '02']

filee = open('slash_february.txt', 'w', encoding='utf-8')
filee.write('\n'.join(slash_february))
filee.close()
