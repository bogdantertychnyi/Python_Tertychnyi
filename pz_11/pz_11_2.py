# Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно вставив после строки N (N – задается пользователем)
# произвольную фразу.


inputfile = 'text18-28.txt'
outputfile = 'new_text.txt'
f = open(inputfile, 'r', encoding='utf-16')
content = f.read()
f.close()
print("Содержимое файла:")
print(content)
num_characters = len(content)
print(f"\nКоличество символов в тексте: {num_characters}")

N = int(input("Введите номер строки для вставки фразы: ")) - 1
phrase = input("Введите произвольную фразу для вставки: ")

lines = content.splitlines()

lines.insert(N + 1, phrase)  # Вставляем после N, поэтому используем N + 1

new_content = '\n'.join(lines)

f = open(outputfile, 'w', encoding='utf-8')
f.write(new_content)
f.close()

