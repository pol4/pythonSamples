x_orig=""
while not(x_orig.upper()==('exit').upper()):
    print("Введите число: (для выхода введите Exit)")
    try:
       x_orig = input()
       if (x_orig.upper()==('exit').upper()):
           break
       x = int(x_orig)
       print("Введено число: ", x, "\nТип данных: ", type(x))
    except ValueError:
       print("Эту фигню ввёл:", x_orig, "\nПопробуй ещё раз. (для выхода введите Exit)")
print("Заходи если что...")
exit(0)
#    while not (x := input_digital()):
#        print("Фигню ввёл. Попробуй ещё раз")
#
#print("Введено число: ", x, "\nТип данных: ", type(x))