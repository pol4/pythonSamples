def input_digital():
    x_orig = input()
    if x_orig.isdecimal():
        return int(x_orig)
    else:
        return False

def main():
    print("Введите число: ")

    while (x := input_digital()) == False:
        print("Фигню ввёл. Попробуй ещё раз.")

    print("Введено число: ", x)


if __name__ == "__main__":
    main()
