num = input('введите номер дня недели ')
while type(num) != int:
  try:
    num = int(num)
    if num == 1:
      print("понедельник")
    elif num == 2:
      print("вторник")
    elif num == 3:
      print("среда")
    elif num == 4:
      print("четверг")
    elif num == 5:
      print("пятница")
    elif num == 6:
      print("суббота")
    elif num == 7:
      print("воскресенье")
    else:
      print("введите число от 1 до 7 ")
      num = input('введите номер дня недели ')
  except ValueError:
    print("Неправильно ввели!")
    num = input('введите номер дня недели ')
