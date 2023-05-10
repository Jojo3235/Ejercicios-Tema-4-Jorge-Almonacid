# Ejercicio 3

# Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de agujas (o desvíos).
# Contemplar las siguientes consideraciones:
# cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre,
# en el caso de los desvíos el nombre es un número –estos estarán numerados de manera consecutiva-;
# cada desvío puede tener múltiples puntos de entrada y salida;
# se deben cargar seis estaciones de trenes y doce cambios de agujas;
# cada cambio de aguja debe tener al menos cuatro salida o vértices adyacentes;
# y cada estación como máximo dos salidas o llegadas y no puede haber dos estaciones co- nectadas directamente;
# encontrar el camino más corto desde:
# la estación King's Cross hasta la estación Waterloo,
# la estación Victoria Train Station hasta la estación Liverpool Street Station,
# la estación St. Pancras hasta la estación King's Cross;

import heapq

# Definir el grafo
graph = {
    'King\'s Cross': {'Euston': 1, 'Farringdon': 2},
    'Euston': {'King\'s Cross': 1, 'Camden Town': 1},
    'Farringdon': {'King\'s Cross': 2, 'Liverpool Street Station': 2, 'Barbican': 1},
    'Camden Town': {'Euston': 1, 'Chalk Farm': 1},
    'Chalk Farm': {'Camden Town': 1, 'Hampstead Heath': 2},
    'Hampstead Heath': {'Chalk Farm': 2, 'Golders Green': 3},
    'Golders Green': {'Hampstead Heath': 3, 'Finchley Central': 4},
    'Finchley Central': {'Golders Green': 4, 'High Barnet': 5},
    'High Barnet': {'Finchley Central': 5},
    'Barbican': {'Farringdon': 1, 'Moorgate': 1},
    'Moorgate': {'Barbican': 1, 'Liverpool Street Station': 1},
    'Liverpool Street Station': {'Farringdon': 2, 'Moorgate': 1, 'Whitechapel': 2, 'Victoria Train Station': 4},
    'Whitechapel': {'Liverpool Street Station': 2, 'Shadwell': 1},
    'Shadwell': {'Whitechapel': 1, 'Bank': 3},
    'Bank': {'Shadwell': 3, 'Waterloo': 4},
    'Waterloo': {'Bank': 4},
    'Victoria Train Station': {'Westminster': 2, 'Pimlico': 1, 'Liverpool Street Station': 4},
    'Westminster': {'Victoria Train Station': 2, 'Waterloo': 2},
    'Pimlico': {'Victoria Train Station': 1, 'Vauxhall': 2},
    'Vauxhall': {'Pimlico': 2, 'Clapham Junction': 4},
    'Clapham Junction': {'Vauxhall': 4, 'Balham': 3, 'Wimbledon': 6},
    'Balham': {'Clapham Junction': 3, 'Tooting Bec': 2},
    'Tooting Bec': {'Balham': 2, 'Tooting Broadway': 1},
    'Tooting Broadway': {'Tooting Bec': 1, 'Colliers Wood': 1},
    'Colliers Wood': {'Tooting Broadway': 1, 'South Wimbledon': 1},
    'South Wimbledon': {'Colliers Wood': 1, 'Wimbledon': 1},
    'Wimbledon': {'South Wimbledon': 1, 'Clapham Junction': 6},
    'St. Pancras': {'King\'s Cross': 1}
}

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while len(queue) > 0:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances[end]

print('La distancia más corta entre King\'s Cross y Waterloo es: ', dijkstra(graph, 'King\'s Cross', 'Waterloo'))
print('La distancia más corta entre King\'s Cross y St.Pancras es: ', dijkstra(graph, 'St. Pancras', 'King\'s Cross' ))
