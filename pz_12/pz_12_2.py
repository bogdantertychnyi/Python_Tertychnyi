#Составить генератор (yield), который переведет символы строки из верхнего
#регистра в нижний.

def smaller(string):
    lowerc = map(lambda c: c.lower(), string)
    for c in lowerc:
        yield c

stroka = input("Введите строку: ")

small = smaller(stroka)

for a in small:
    print(a, end='')
