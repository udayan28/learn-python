#! python3
# コラッツ数列

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


try:
    num = int(input())
    while num > 1:
        num = collatz(num)
        print(num)
except ValueError:
    print('数値を入力してください')