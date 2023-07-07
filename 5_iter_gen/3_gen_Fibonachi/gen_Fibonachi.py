# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def fibonachi(n):
    fib1, fib2 = 0, 1
    while n:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

def main():
    for i in fibonachi(10):
        print(i, end=' ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
