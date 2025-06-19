# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Среднее арифметическое элементов первого и второго файлов:
# Количество нечетных элементов первого и второго файлов:
# Элементы общие для двух файлов:
# Количество элементов, общих для двух файлов:


file1 = open('list1.txt', 'w')
file1.write('60 13 2 -8 10 18 -8 94 58')
file1.close()

file2 = open('list2.txt', 'w')
file2.write('2 20 17 44 -1 90 63 100 -8')
file2.close()

file1 = open('list1.txt', 'r')
el = file1.read().split()
elint = []
for i in el:
    elint.append(int(i))
file1.close()

file2 = open('list2.txt', 'r')
el2 = file2.read().split()
elint2 = []
for i in el2:
    elint2.append(int(i))
file2.close()

srael1 = sum(elint) / len(elint)
srael2 = sum(elint2) / len(elint2)

el21 = 0
for i in elint:
    if i % 2 != 0:
        el21 += 1

el22 = 0
for i in elint2:
    if i % 2 != 0:
        el22 += 1

obsh_el = set(elint) & set(elint2)
obsh_el_count = len(obsh_el)

obsh_el_str = ' '.join([str(i) for i in obsh_el])

with open('results.txt', 'w', encoding='UTF-8') as results:
    results.write('Элементы первого файла: ' + ' '.join(el) + '\n')
    results.write('Элементы второго файла: ' + ' '.join(el2) + '\n')
    results.write(f'Среднее арифметическое элементов первого файла: {srael1}\n')
    results.write(f'Среднее арифметическое элементов второго файла: {srael2}\n')
    results.write(f'Количество нечетных элементов первого файла: {el21}\n')
    results.write(f'Количество нечетных элементов второго файла: {el22}\n')
    results.write('Общие элементы: ' + obsh_el_str + '\n')
    results.write(f'Количество общих элементов: {obsh_el_count}\n')
