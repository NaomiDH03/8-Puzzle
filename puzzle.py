
#Juego 8-Puzzle por medio de un grafo

class NodeAdy:
    def __init__(self, data):
        self.vertex = data
        self.next = None

# Grafo
class Graph:
    
    def __init__(self, size):
        self.size = size
        self.graph = {}
        self.positions = {} 

    def addVertex(self, data, fila, col):
        if data not in self.graph and len(self.graph) < self.size:
            self.graph[data] = []
            self.positions[data] = (fila, col)
        else:
            print("Ya no se puede")
        #print(self.graph)

    def add_edge(self, v, w):
        
        if self.graph[v] == []:
            self.graph[v] = NodeAdy(w)  # Lista asociada a v
            
        if self.graph[w] == []:
            self.graph[w] = NodeAdy(v)  # Lista asociada a w
          
        #Para agregar a un diccionario existente    
        if self.graph[v] != []:  # Si no está vacío
            nodo = self.graph[v]
            while nodo.next != None:
                nodo = nodo.next
            if nodo.vertex != w:
                nodo.next = NodeAdy(w)
         
        #Para agregar a un diccionario existente pero en espejo       
        if self.graph[w] != []:
            nodo = self.graph[w]
            while nodo.next != None:
                nodo = nodo.next
            if nodo.vertex != v:
                nodo.next = NodeAdy(v)
        nodito = self.graph[v]
        
        while nodito != None:
            nodito = nodito.next
        
    def mostrar_grafo_3x3(self):
        show = []
        for i in range(3):
            fila = []
            for j in range(3):
                fila.append(' ')
            show.append(fila)

        for vertex, (fila, col) in self.positions.items():
            show[fila][col] = vertex

        for fila in show:
            print('  '.join(fila))
          
            
    def puzzle(self, pieza):
        #Iniciamos con la pieza 6 y la movemos abajo
        #Queda 2 8 3 | 1 _ 4 | 7 6 5
        #Después movemos el 8 hacia abajo 
        #Queda 2 _ 3 | 1 8 4 | 7 6 5
        pass
          

        
grafo = Graph(9)
grafo.addVertex('2', 0, 0)
grafo.addVertex('8', 0, 1)
grafo.addVertex('3', 0, 2)

grafo.addVertex('1', 1, 0)
grafo.addVertex('6', 1, 1)
grafo.addVertex('4', 1, 2)

grafo.addVertex('7', 2, 0)
grafo.addVertex('_', 2, 1)
grafo.addVertex('5', 2, 2)

#Nota: Ahorita los pesos estan de adorno
grafo.add_edge('2', '8', 2)
grafo.add_edge('2', '1', 3)
grafo.add_edge('8', '2', 4)
grafo.add_edge('8', '6', 5)
grafo.add_edge('8', '3', 6)
grafo.add_edge('1', '2', 7)
grafo.add_edge('1', '6', 8)
grafo.add_edge('1', '7', 9)
grafo.add_edge('6', '1', 10)
grafo.add_edge('6', '8', 11)
grafo.add_edge('6', '4', 12)
grafo.add_edge('6', '_', 1)
grafo.add_edge('4', '6', 13)
grafo.add_edge('4', '5', 14)
grafo.add_edge('7', '1', 15)
grafo.add_edge('7', '_', 16)
grafo.add_edge('_', '7', 17)
grafo.add_edge('_', '6', 18)
grafo.add_edge('_', '5', 19)
grafo.add_edge('5', '_', 20)
grafo.add_edge('5', '4', 21)

grafo.mostrar_grafo_3x3()
#grafo.puzzle(6)


