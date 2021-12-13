import collections

grafo = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visitados = set() 

def bfs(visitados, grafo, nodo):

    cola = collections.deque([nodo])
    visitados.add(nodo)

    while cola:
        nodo_a_visitar = cola.popleft()
        print(f"visite: {nodo_a_visitar}")
        for vecino in grafo[nodo_a_visitar]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)


bfs(visitados, grafo, '5')