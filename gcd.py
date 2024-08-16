
def input_digital():
    x_orig = input()
    if x_orig.isdecimal():
        return int(x_orig)
    else:
        return "NaN"


def gcd(n, m) -> int:
    if n==m:
        print("Last call")
        return n
    else:
        x=max([n, m])
        y=min([n, m])
        n=x-y
        m=y
        return gcd(n,m)

def fn(x, y):
    return x if y<x else y

def expn(x, y):
    if x==0:
        return 0
    if y==0:
        return 1
    if y<2:
        print("Last")
        return x
    else:
        return x*expn(x, y-1)

def main():
    print("Введите число x: ")

    while (x := input_digital())=="NaN":
        print("Фигню ввёл. Попробуй ещё раз.")

    print("Введено число: ", x)

    print("Введите число y: ")

    while (y := input_digital())=="NaN":
        print("Фигню ввёл. Попробуй ещё раз.")

    print("Введено число: ", y)

    print(gcd(x, y))
    #print(fn(x, y))
    #print(expn(x, y))

if __name__ == "__main__":
    main()
