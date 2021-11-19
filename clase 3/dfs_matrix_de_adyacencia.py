visitados = set()

def dfs(visitados, grafo,nodo):
    if nodo not in visitados:
        print (nodo)
        visitados.add(nodo)
        for vecino in range(len(grafo[nodo])):
            if(grafo[nodo][vecino]>0):
                dfs(visitados,grafo,vecino)

grafo = [
    [0,8,0,3,0],
    [0,0,7,0,0],
    [0,0,0,0,4],
    [0,0,0,0,3],
    [0,0,5,0,0]
]

dfs(visitados, grafo, 0)