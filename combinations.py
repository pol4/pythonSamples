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

def combinations(n: int, M: int, result=[], prefix=None) -> list:
    if M==0:
        print(prefix)
        print(type(prefix))
        result.append(list(prefix))
        return
    prefix = prefix or []
    #result = result or []
    for a in range(n):
        prefix.append(a)
        combinations(n, M-1, result, prefix)
        prefix.pop()
    return result

def main():
    print("Введите число x: ")

    while (x := input_digital())=="NaN":
        print("Фигню ввёл. Попробуй ещё раз.")

    print("Введено число: ", x)

    #total_list = []

    #print(gcd(x, y))
    print("Total list is: ", combinations(9, x))
    #print(total_list)
    #print(fn(x, y))
    #print(expn(x, y))

if __name__ == "__main__":
    main()
