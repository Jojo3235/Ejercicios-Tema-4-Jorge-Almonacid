import heapq

# Construimos el grafo como un diccionario de listas
grafo = {
    'King\'s Cross': ['St. Pancras', 'Waterloo', '1', '2', '6'],
    'St. Pancras': ['King\'s Cross', '1', '2', '11'],
    'Victoria Train Station': ['3', '4', '5', '6'],
    'Waterloo': ['King\'s Cross', '5', '6', '7', '8', '9', '10', '11', '12'],
    'Liverpool Street Station': ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    '1': ['King\'s Cross', '2', '3', '4', '5', '6'],
    '2': ['King\'s Cross', '1', '3', '4', '5', '6'],
    '3': ['1', '2', 'Liverpool Street Station', 'Victoria Train Station'],
    '4': ['1', '2', 'Liverpool Street Station', 'Victoria Train Station'],
    '5': ['1', '2', 'Liverpool Street Station', 'Waterloo', 'Victoria Train Station'],
    '6': ['1', '2', 'Liverpool Street Station', 'Waterloo', 'King\'s Cross'],
    '7': ['1', '2', 'Liverpool Street Station', 'Waterloo', '3'],
    '8': ['1', '2', 'Liverpool Street Station', 'Waterloo', '4'],
    '9': ['1', '2', 'Liverpool Street Station', 'Waterloo', '5'],
    '10': ['1', '2', 'Liverpool Street Station', 'Waterloo', '2'],
    '11': ['1', '2', 'Liverpool Street Station', 'Waterloo', '6'],
    '12': ['1', '2', 'Liverpool Street Station', 'Waterloo', '11'],
}

# Definimos una función para encontrar el camino más corto entre dos estaciones utilizando Dijkstra
def dijkstra_camino_mas_corto(origen, destino):
    # Verificamos si las estaciones existen en el grafo
    if origen not in grafo or destino not in grafo:
        return []

    # Definimos una función de costo para las aristas
    def costo(a, b):
        return 1  # Todas las aristas tienen el mismo costo

    # Utilizamos el algoritmo de Dijkstra para encontrar el camino más corto
    heap = [(0, origen)]
    visitados = set()
    padres = {}
    distancias = {origen: 0}
    while heap:
        (dist, v) = heapq.heappop(heap)
        if v in visitados:
            continue
        visitados.add(v)
        if v == destino:
            # Si llegamos al destino, construimos el camino de regreso
            camino = [destino]
            while camino[-1] != origen:
                camino.append(padres[camino[-1]])
            camino.reverse()
            return camino
        for w in grafo[v]:
            if w in visitados:
                continue
            if w not in distancias or distancias[w] > dist + costo(v, w):
                distancias[w] = dist + costo(v, w)
                padres[w] = v
                heapq.heappush(heap, (distancias[w], w))

    # Si no se encontró un camino, devolvemos una lista vacía
    return []

def main():
    # Definimos las estaciones de origen y destino
    origen = 'King\'s Cross'
    destino = 'Waterloo'

    origen_2 = 'Victoria Train Station'
    destino_2 = 'Liverpool Street Station'

    origen_3 = 'St. Pancras'
    destino_3 = 'King\'s Cross'

    # Encontramos el camino más corto entre las estaciones utilizando Dijkstra
    camino = dijkstra_camino_mas_corto(origen, destino)
    print('El camino más corto entre {} y {} es: {}'.format(origen, destino, camino))
    print("Distancia: ", len(camino) - 1, " estaciones")

    camino_2 = dijkstra_camino_mas_corto(origen_2, destino_2)
    print('El camino más corto entre {} y {} es: {}'.format(origen_2, destino_2, camino_2))
    print("Distancia: ", len(camino_2) - 1, " estaciones")

    camino_3 = dijkstra_camino_mas_corto(origen_3, destino_3)
    print('El camino más corto entre {} y {} es: {}'.format(origen_3, destino_3, camino_3))
    print("Distancia: ", len(camino_3) - 1, " estaciones")

if __name__ == '__main__':
    main()