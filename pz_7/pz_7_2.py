# Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
# расположенную между первым и последним пробелом исходной строки. Если
# строка содержит только один пробел, то вывести пустую строку.

S = input('Введите строку:')
cpr = S.count(" ")    # количество пробелов
start = S.find(" ") + 1
end = S.rfind(" ")
if cpr > 1:
    S1 = S[start:end]    # новая строка
else:
    S1 = ""
print(S1)
