import matplotlib.pyplot as plt
import math

def input_digital():
    x_orig = input()
    if x_orig.isdecimal():
        return int(x_orig)
    else:
        return False

def recurs(n):
    if n==1:
        print("Last rec n=", n)
    else:
        print("Top rec n=",n)
        recurs(n-1)
        print("Bottom rec n=",n)


def draw_lines(a,b,c,d):
    plt.plot(a, b)
    plt.plot(b, c)
    plt.plot(c, d)
    plt.plot(d, a)


def gra_req(n=10, x0=0, y0=0, dl=200):
    if n<1:
        print("Deepest")
    else:
        print("Enter n=", n)
        draw_lines((x0, y0),(x0, y0+dl),(x0+dl, y0+dl),(x0+dl, y0))
        draw_lines((x0, y0+dl/2), (x0+dl/2, y0 + dl), (x0 + dl, y0 + dl/2), (x0 + dl/2, y0))
        x0=x0+dl/4
        y0=y0+dl/4
        dl=dl/2
        gra_req(n - 1, x0, y0, dl)
        print("Exit n=", n)



def main():
#    print("Введите количество матрёшек: ")

 #   while (x := input_digital()) == False:
 #       print("Фигню ввёл. Попробуй ещё раз.")

 #   print("Введено число: ", x)

 #   recurs(x)
    gra_req(100,0, 0, 1000)

#    draw_lines(0, 0, 0, 200, 200,200,200,0)

#    draw_lines(0, 100, 100, 200, 200, 100, 100, 0)

    plt.show()

if __name__ == "__main__":
    main()
