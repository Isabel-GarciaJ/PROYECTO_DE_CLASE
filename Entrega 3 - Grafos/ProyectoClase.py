import math
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}

    def agregar_vecino(self, vecino, peso):
        self.vecinos[vecino] = peso

    def eliminar_vecino(self, vecino):
        if vecino in self.vecinos:
            del self.vecinos[vecino]

    def obtener_grado(self):
        return len(self.vecinos)

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)

    def eliminar_nodo(self, nombre):
        if nombre in self.nodos:
            for nodo in self.nodos.values():
                nodo.eliminar_vecino(nombre)
            del self.nodos[nombre]

    def agregar_arista(self, origen, destino, peso):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        self.nodos[origen].agregar_vecino(destino, peso)
        self.nodos[destino].agregar_vecino(origen, peso)

    def eliminar_arista(self, origen, destino):
        if origen in self.nodos:
            self.nodos[origen].eliminar_vecino(destino)
        if destino in self.nodos:
            self.nodos[destino].eliminar_vecino(origen)

    def dijkstra(self, inicio):
        distancias = {nodo: math.inf for nodo in self.nodos}
        anteriores = {nodo: None for nodo in self.nodos}
        distancias[inicio] = 0
        visitados = set()
        heap = [(0, inicio)]

        while heap:
            distancia_actual, nodo_actual = heapq.heappop(heap)

            if nodo_actual in visitados:
                continue
            visitados.add(nodo_actual)

            for vecino, peso in self.nodos[nodo_actual].vecinos.items():
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual
                    heapq.heappush(heap, (nueva_distancia, vecino))

        return distancias, anteriores

    def visualizar_grafo(self):
        G = nx.Graph()
        for nombre, nodo in self.nodos.items():
            for vecino, peso in nodo.vecinos.items():
                if not G.has_edge(nombre, vecino):
                    G.add_edge(nombre, vecino, weight=peso)
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Red de Entrega - Supermercado La Última Lágrima")
        plt.show()
    
    def visualizar_camino(self, camino):
        if not camino or len(camino) < 2:
            print("No hay camino válido para mostrar.")
            return

        G = nx.Graph()
        for nombre, nodo in self.nodos.items():
            for vecino, peso in nodo.vecinos.items():
                G.add_edge(nombre, vecino, weight=peso)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        edge_colors = []
        edge_list = []

        for edge in G.edges():
            if edge in zip(camino, camino[1:]) or (edge[1], edge[0]) in zip(camino, camino[1:]):
                edge_colors.append('red')  # Camino más corto
            else:
                edge_colors.append('black')  # Conexiones normales
            edge_list.append(edge)

        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color=edge_colors, width=2)

        plt.title("Ruta más corta destacada")
        plt.show()

def reconstruir_camino(anteriores, inicio, destino):
        camino = []
        actual = destino
        while actual is not None:
            camino.insert(0, actual)
            actual = anteriores[actual]
        if camino[0] == inicio:
            return camino
        else:
            return None  # No hay camino
        
# Sistema de interacción por consola
def menu(grafo):
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar sucursal")
        print("2. Eliminar sucursal")
        print("3. Agregar conexión entre sucursales")
        print("4. Eliminar conexión")
        print("5. Calcular rutas desde una sucursal")
        print("6. Visualizar grafo")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la nueva sucursal: ")
            grafo.agregar_nodo(nombre)

        elif opcion == '2':
            nombre = input("Nombre de la sucursal a eliminar: ")
            grafo.eliminar_nodo(nombre)

        elif opcion == '3':
            origen = input("Sucursal origen: ")
            destino = input("Sucursal destino: ")
            peso = float(input("Distancia (peso): "))
            grafo.agregar_arista(origen, destino, peso)

        elif opcion == '4':
            origen = input("Sucursal origen: ")
            destino = input("Sucursal destino: ")
            grafo.eliminar_arista(origen, destino)

        elif opcion == '5':
            inicio = input("Sucursal de inicio: ")
            destino = input("Sucursal destino: ")
            if inicio not in grafo.nodos or destino not in grafo.nodos:
                print("Una o ambas sucursales no existen.")
            else:
                distancias, anteriores = grafo.dijkstra(inicio)
                camino = reconstruir_camino(anteriores, inicio, destino)
            if camino:
                print(f"Ruta más corta de {inicio} a {destino}: {' -> '.join(camino)}")
                print(f"Distancia total: {distancias[destino]}")
                grafo.visualizar_camino(camino)
            else:
                print(f"No hay camino disponible de {inicio} a {destino}.")

        elif opcion == '6':
            grafo.visualizar_grafo()

        elif opcion == '0':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

# Crear el grafo y agregar nodos/conexiones iniciales
grafo = Grafo()
grafo.agregar_arista('A', 'B', 5)
grafo.agregar_arista('A', 'C', 10)
grafo.agregar_arista('B', 'D', 3)
grafo.agregar_arista('C', 'D', 4)
grafo.agregar_arista('D', 'E', 2)
grafo.agregar_arista('B', 'E', 9)

menu(grafo)
