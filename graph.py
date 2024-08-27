# Iñigo Quintana Delgadillo
# Naomi Díaz Hurtado
# 27/08/2024

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
          self.matriz_meta = [[1, 2, 3], 
                              [8, 0, 4], 
                              [7, 6, 5]]

     def agregar_nodo(self, valor):
          if valor not in self.nodos:
               self.nodos[valor] = Nodo(valor)


     def agregar_arista(self, valor1, valor2):
          if valor1 in self.nodos and valor2 in self.nodos:
               self.nodos[valor1].agregar_vecino(self.nodos[valor2])
               self.nodos[valor2].agregar_vecino(self.nodos[valor1])  # Si es un grafo no dirigido


     def construir_matriz(self, matriz):
          self.matriz = matriz
          for i in range(len(self.matriz)):
               for j in range(len(self.matriz)):
                    valor = matriz[i][j]
                    self.agregar_nodo(valor)
          print("Matriz de nodos:", self.matriz)
               
          for i in range(len(self.matriz)):
               for j in range(len(self.matriz)):
                    nodo_actual = self.matriz[i][j]
                    
                    # Nodo de arriba
                    if i > 0:
                         self.agregar_arista(nodo_actual, self.matriz[i-1][j])
                    
                    # Nodo de abajo
                    if i < len(self.matriz) - 1:
                         self.agregar_arista(nodo_actual, self.matriz[i+1][j])
                    
                    # Nodo de la izquierda
                    if j > 0:
                         self.agregar_arista(nodo_actual, self.matriz[i][j-1])
                    
                    # Nodo de la derecha
                    if j < len(self.matriz) - 1:
                         self.agregar_arista(nodo_actual, self.matriz[i][j+1])


     def actualizar_vecinos(self):
          # Reiniciar los vecinos de todos los nodos
          for nodo in self.nodos.values():
               nodo.vecinos = []

          # Volver a conectar los nodos en función de la matriz actual
          for i in range(len(self.matriz)):
               for j in range(len(self.matriz[i])):
                    valor_actual = self.matriz[i][j]

                    # Nodo de arriba
                    if i > 0:
                         self.agregar_arista(valor_actual, self.matriz[i - 1][j])
                    # Nodo de abajo
                    if i < len(self.matriz) - 1:
                         self.agregar_arista(valor_actual, self.matriz[i + 1][j])
                    # Nodo de la izquierda
                    if j > 0:
                         self.agregar_arista(valor_actual, self.matriz[i][j - 1])
                    # Nodo de la derecha
                    if j < len(self.matriz[i]) - 1:
                         self.agregar_arista(valor_actual, self.matriz[i][j + 1])
                         

     def estados(self):
          while self.matriz != self.matriz_meta:
               vecinos = self.obtener_vecinos(0)
               print("Vecinos:", vecinos)
               
               # Encuentra las coordenadas del 0 en la matriz
               coords_0 = None
               for i in range(len(self.matriz)):
                    for j in range(len(self.matriz)):
                         if self.matriz[i][j] == 0:
                              coords_0 = (i, j)
                              break
                    if coords_0:
                         break
               
               if not coords_0:
                    print("No se encontró el 0 en la matriz")
                    return
               
               i_0, j_0 = coords_0

               # Generar todas las combinaciones posibles al intercambiar el 0 con cada vecino
               combinaciones = []
               for vecino in vecinos:
                    for i in range(len(self.matriz)):
                         for j in range(len(self.matriz)):
                              if self.matriz[i][j] == vecino:
                                   nueva_matriz = [fila[:] for fila in self.matriz]  # Copiar la matriz
                                   nueva_matriz[i_0][j_0], nueva_matriz[i][j] = nueva_matriz[i][j], nueva_matriz[i_0][j_0]
                                   combinaciones.append(nueva_matriz)
               # print(combinaciones)

               movimientos = []
               for i in range(len(combinaciones)):
                    movimientos.append(self.comparar_matrices(combinaciones[i], self.matriz_meta))
               # print(movimientos)
               
               for i in range(len(movimientos)):
                    if movimientos[i] == min(movimientos):
                         print("\nMovimientos:", movimientos[i])
                         print("Matriz:")
                         for fila in combinaciones[i]:
                              print(fila)

                         self.matriz = combinaciones[i]
                         break

               # Actualizar los vecinos de todos los nodos
               self.actualizar_vecinos()
          

     def comparar_matrices(self, matriz_actual, matriz_meta):
          movimientos = 0
          for i in range(len(matriz_actual)):
               for j in range(len(matriz_actual[i])):
                    valor_actual = matriz_actual[i][j]
                    
                    # Encontrar la posición correcta del valor actual en la matriz meta
                    for x in range(len(matriz_meta)):
                         for y in range(len(matriz_meta[x])):
                              if matriz_meta[x][y] == valor_actual:
                                   movimientos += abs(i - x) + abs(j - y)
          return movimientos


     def obtener_vecinos(self, valor):
          if valor in self.nodos:
               return [vecino.valor for vecino in self.nodos[valor].vecinos]
          return []

     def __str__(self):
          return "\n".join([str(nodo) for nodo in self.nodos.values()])
     

# Ejemplo de uso
mi_grafo = Grafo()

matriz = [[2, 8, 3], 
          [1, 6, 4], 
          [7, 0, 5]]

mi_grafo.construir_matriz(matriz)
mi_grafo.estados()