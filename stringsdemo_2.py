def input_digital():
    try:
        x_orig = input()
        x = int(x_orig)
        return x
    except ValueError:
        return False


def main():
    print("Введите число:")

    while not (x := input_digital()):
        print("Фигню ввёл. Попробуй ещё раз")

    print("Введено число: ", x, "\nТип данных: ", type(x))

if __name__ == '__main__':
    main()
