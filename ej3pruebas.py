class Node:
    def __init__(self, name, tipo):
        self.name = name
        self.tipo = tipo
        self.vecinos = {}

    def agregar_vecino(self, vecino, peso):
        self.vecinos[vecino] = peso


class Arista:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso


# graph = {
#     'King\'s Cross': {'Euston': 1, 'Farringdon': 2},
#     'Euston': {'King\'s Cross': 1, 'Camden Town': 1},
#     'Farringdon': {'King\'s Cross': 2, 'Liverpool Street Station': 2, 'Barbican': 1},
#     'Camden Town': {'Euston': 1, 'Chalk Farm': 1},
#     'Chalk Farm': {'Camden Town': 1, 'Hampstead Heath': 2},
#     'Hampstead Heath': {'Chalk Farm': 2, 'Golders Green': 3},
#     'Golders Green': {'Hampstead Heath': 3, 'Finchley Central': 4},
#     'Finchley Central': {'Golders Green': 4, 'High Barnet': 5},
#     'High Barnet': {'Finchley Central': 5},
#     'Barbican': {'Farringdon': 1, 'Moorgate': 1},
#     'Moorgate': {'Barbican': 1, 'Liverpool Street Station': 1},
#     'Liverpool Street Station': {'Farringdon': 2, 'Moorgate': 1, 'Whitechapel': 2, 'Victoria Train Station': 4},
#     'Whitechapel': {'Liverpool Street Station': 2, 'Shadwell': 1},
#     'Shadwell': {'Whitechapel': 1, 'Bank': 3},
#     'Bank': {'Shadwell': 3, 'Waterloo': 4},
#     'Waterloo': {'Bank': 4},
#     'Victoria Train Station': {'Westminster': 2, 'Pimlico': 1, 'Liverpool Street Station': 4},
#     'Westminster': {'Victoria Train Station': 2, 'Waterloo': 2},
#     'Pimlico': {'Victoria Train Station': 1, 'Vauxhall': 2},
#     'Vauxhall': {'Pimlico': 2, 'Clapham Junction': 4},
#     'Clapham Junction': {'Vauxhall': 4, 'Balham': 3, 'Wimbledon': 6},
#     'Balham': {'Clapham Junction': 3, 'Tooting Bec': 2},
#     'Tooting Bec': {'Balham': 2, 'Tooting Broadway': 1},
#     'Tooting Broadway': {'Tooting Bec': 1, 'Colliers Wood': 1},
#     'Colliers Wood': {'Tooting Broadway': 1, 'South Wimbledon': 1},
#     'South Wimbledon': {'Colliers Wood': 1, 'Wimbledon': 1},
#     'Wimbledon': {'South Wimbledon': 1, 'Clapham Junction': 6},
#     'St. Pancras': {'King\'s Cross': 1}
# }

import heapq

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, node1, node2, weight):
        if node1.name not in self.nodes:
            self.add_node(node1)
        if node2.name not in self.nodes:
            self.add_node(node2)

        if node1.name not in self.edges:
            self.edges[node1.name] = {}
        self.edges[node1.name][node2.name] = weight

    def shortest_path(self, start_node_name, end_node_name):
        distances = {}
        predecessors = {}
        heap = []

        for node in self.nodes.values():
            distances[node.name] = float('inf')
            predecessors[node.name] = None
            if node.name == start_node_name:
                distances[node.name] = 0

            heapq.heappush(heap, (distances[node.name], node))

        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_distance == float('inf'):
                break

            for neighbor_name, weight in self.edges.get(curr_node.name, {}).items():
                distance = distances[curr_node.name] + weight
                if distance < distances[neighbor_name]:
                    distances[neighbor_name] = distance
                    predecessors[neighbor_name] = curr_node.name

                    for i, (distance, node) in enumerate(heap):
                        if node.name == neighbor_name:
                            heap[i] = (distance, node)
                            break
                    else:
                        heapq.heappush(heap, (distance, self.nodes[neighbor_name]))

        path = []
        curr_name = end_node_name
        while curr_name != start_node_name:
            path.append(curr_name)
            curr_name = predecessors[curr_name]
        path.append(start_node_name)

        return list(reversed(path)), distances[end_node_name]


graph = Graph()

# Agregar nodos
graph.add_node(Node('King\'s Cross', 'estacion'))
graph.add_node(Node('Euston', 'estacion'))
graph.add_node(Node('Farringdon', 'estacion'))
# agregar más nodos...

# Agregar aristas
graph.add_edge(Node('King\'s Cross', 'estacion'), Node('Euston', 'estacion'), 1)
graph.add_edge(Node('King\'s Cross', 'estacion'), Node('Farringdon', 'estacion'), 2)
# agregar más aristas...

# Encontrar el camino más corto
path, distance = graph.shortest_path('King\'s Cross', 'Waterloo')
print(f"Camino más corto: {path}")
print(f"Distancia: {distance}")