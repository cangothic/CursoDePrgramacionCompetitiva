def busqueda_binaria_recursiva(arreglo, busqueda, izquierda, derecha):
    if izquierda > derecha:
        return -1
    indiceDelElementoDelMedio = (izquierda + derecha) // 2
    elementoDelMedio = arreglo[indiceDelElementoDelMedio]
    if elementoDelMedio == busqueda:
        return indiceDelElementoDelMedio
    if busqueda < elementoDelMedio:
        return busqueda_binaria_recursiva(arreglo, busqueda, izquierda, indiceDelElementoDelMedio - 1)
    else:
        return busqueda_binaria_recursiva(arreglo, busqueda, indiceDelElementoDelMedio + 1, derecha)


arreglo = [1,3,7,8,10,44]

indice = busqueda_binaria_recursiva(arreglo,7,0,len(arreglo))

print(indice)