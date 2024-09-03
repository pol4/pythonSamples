import random as rnd

def f1(a) -> list:
    #a=None or []
    a.append(1)
    return a


def main():
    a = [rnd.randint(1,100) for i in range(1000)]
    #a.sort()
    #print(sorted(a))
    #b = [[0] * 5 for i in range(10)]
    #print(b)
    a=[]
    #print(f1(f1(f1(1))))
    print(f1(a))
    print(f1(a))
    print(f1(a))
if __name__ == "__main__":
    main()
