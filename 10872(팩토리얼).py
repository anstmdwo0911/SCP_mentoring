#팩토리얼


#2
def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(int(input())))

'''
#3
def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)
sum=int(input())
print(factorial(sum))

'''
