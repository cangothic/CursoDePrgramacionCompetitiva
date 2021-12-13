memorizacion = [0 for _ in range(100)]
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memorizacion[n] == 0:
        memorizacion[n] = fib(n-1) + fib(n-2)
    return memorizacion[n]

for i in range(99):
    print(fib(i))