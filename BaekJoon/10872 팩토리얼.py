def factorial(x):
    if x>0:
        return x*factorial(x-1)
    else:
        return 1

n=int(input())
result=factorial(n)

print(result)