
memorizacion = [0,1]

def fib(n):
    maximo_calculado = len(memorizacion)-1
    if len(memorizacion)-1 == n:
        return memorizacion[n]
    while(maximo_calculado < n):
        maximo_calculado +=1
        calculo = memorizacion[maximo_calculado-1]+memorizacion[maximo_calculado-2]
        memorizacion.append(calculo)
    return memorizacion[n]

for i in range(10):
    print(fib(i))