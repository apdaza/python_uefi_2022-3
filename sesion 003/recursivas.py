# 1, 1, 2, 3, 5, 8, 13, 21, .....
"""
fibo(0) -> 1
fibo(1) -> 1
...
fibo(n) -> fibo(n - 1) + fibo(n - 2) 

fibo(3) = fibo(3 - 1) + fibo(3 - 2)
fibo(3) = fibo(2) + fibo(1)
fibo(3) = fibo(2 - 1) + fibo(2 - 2) + fibo(1)
fibo(3) = fibo(1) + fibo(0) + 1
fibo(3) = 1 + 1 + 1
fibo(3) = 3

"""

def fibo(n):
    if n in [0, 1]:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibo_iterativo(n):
    if n in [0, 1]:
        return 1
    else:
        t0 = 1
        t1 = 1
        cont = 2
        while cont <= n:
            t0, t1 = t1, t0 + t1
            cont += 1
        return t1

print(fibo_iterativo(3))
print(fibo(3))
