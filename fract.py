

def input_digital():
    x_orig = input()
    if x_orig.isdecimal():
        return int(x_orig)
    else:
        return False


def fact(n) -> int:
#    assert n>=2, "Not defined var"
    if n<2:
        print("Last call")
        return 1
    print("Call n=", n)
    return n*fact(n-1)


def main():
    print("Введите число: ")

    while not (x := input_digital()):
        print("Фигню ввёл. Попробуй ещё раз.")

    print("Введено число: ", x)

    print(fact(x))


if __name__ == "__main__":
    main()
