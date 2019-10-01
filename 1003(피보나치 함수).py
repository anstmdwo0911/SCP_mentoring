zero=0 #함수 안에다 설정하면 계속 0으로 초기화되므로 밖에 설정
one=0 #함수안에 global쓴다 하더라도 밖에다가 전역변수 설정을 해야
def fib(n):
    global zero
    global one
    if n==0:
        zero=zero+1
        return 0
    elif n==1:
        one=one+1
        return 1
    else:
      return fib(n-1)+fib(n-2)
fib(int(input()))
print(zero,one)

