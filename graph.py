class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.vecinos = []

    def agregar_vecino(self, vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)

    def __str__(self):
        return f"Nodo({self.valor}): Vecinos -> {[vecino.valor for vecino in self.vecinos]}"


class Grafo:
     def __init__(self):
          self.nodos = {}
          self.matriz = []

     def agregar_nodo(self, valor):
          if valor not in self.nodos:
               self.nodos[valor] = Nodo(valor)

     def agregar_arista(self, valor1, valor2):
          if valor1 in self.nodos and valor2 in self.nodos:
               self.nodos[valor1].agregar_vecino(self.nodos[valor2])
               self.nodos[valor2].agregar_vecino(self.nodos[valor1])  # Si es un grafo no dirigido

     def construir_matriz(self, filas, columnas):
          for i in range(filas):
               fila = []
               for j in range(columnas):
                    valor = i * columnas + j  # Valor único para cada nodo
                    self.agregar_nodo(valor)
                    fila.append(valor)
               self.matriz.append(fila)
               

          for i in range(filas):
               for j in range(columnas):
                    nodo_actual = self.matriz[i][j]
                    # Conectar con el nodo de arriba
                    if i > 0:
                         nodo_arriba = self.matriz[i-1][j]
                         self.agregar_arista(nodo_actual, nodo_arriba)
                    # Conectar con el nodo de abajo
                    if i < filas - 1:
                         nodo_abajo = self.matriz[i+1][j]
                         self.agregar_arista(nodo_actual, nodo_abajo)
                    # Conectar con el nodo de la izquierda
                    if j > 0:
                         nodo_izquierda = self.matriz[i][j-1]
                         self.agregar_arista(nodo_actual, nodo_izquierda)
                    # Conectar con el nodo de la derecha
                    if j < columnas - 1:
                         nodo_derecha = self.matriz[i][j+1]
                         self.agregar_arista(nodo_actual, nodo_derecha)

     def obtener_nodos(self):
          return list(self.nodos.keys())

     def obtener_vecinos(self, valor):
          if valor in self.nodos:
               return [vecino.valor for vecino in self.nodos[valor].vecinos]
          return []

     def __str__(self):
          return "\n".join([str(nodo) for nodo in self.nodos.values()])
     

# Ejemplo de uso
mi_grafo = Grafo()
mi_grafo.construir_matriz(3, 3)  # Construir una matriz de 3x3

print("Nodos en el grafo:", mi_grafo.obtener_nodos())
print("Vecinos del nodo 4:", mi_grafo.obtener_vecinos(4))  # Nodo central en una matriz 3x3
print("Estructura del grafo:")
print(mi_grafo)