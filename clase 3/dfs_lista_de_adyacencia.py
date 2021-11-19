grafo = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visitados = set() 

def dfs(visitados, grafo, nodo):
    if nodo not in visitados:
        print (nodo)
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            dfs(visitados, grafo, vecino)


dfs(visitados, grafo, '5')