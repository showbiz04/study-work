import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = input()
    a, b = n.split()
    c = int(a) + int(b)
    print(c)

if __name__ == '__main__':
    main()
