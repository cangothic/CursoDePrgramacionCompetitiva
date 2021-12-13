
from collections import deque 
      
# Declaring deque 
cola = deque([])
cola.append("a")
cola.append("b")
desencolado = cola.popleft()
print(desencolado)
print(cola)
