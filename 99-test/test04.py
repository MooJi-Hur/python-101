# fibonacci numbers
# 0 1 1 2 3 5 8 13 21 34
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)



if __name__ == '__main__':
    n = int(input('출력할 갯수 입력 : '))
    print(fibo(n))
