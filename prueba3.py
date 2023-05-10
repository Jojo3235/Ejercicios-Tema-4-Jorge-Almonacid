# Carácter,Cantidad,Frecuencia

# A,11,0.09821428571428571
# B,2,0.017857142857142856
# C,4,0.03571428571428571
# D,3,0.026785714285714284
# E,14,0.125
# G,3,0.026785714285714284
# I,6,0.05357142857142857
# L,6,0.05357142857142857
# M,3,0.026785714285714284
# N,6,0.05357142857142857
# O,7,0.0625
# P,4,0.03571428571428571
# Q,1,0.008928571428571428
# R,10,0.08928571428571429
# S,4,0.03571428571428571
# T,3,0.026785714285714284
# U,4,0.03571428571428571
# V,2,0.017857142857142856
# " ",17,0.15178571428571427
# ",",2,0.017857142857142856

#Realizar codigo huffman para desencriptar 10110100100101010100001010101011010101010010

from heapq import heappush, heappop

class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, otro):
        return self.valor < otro.valor
    
def construir_arbol(codigos):
    heap = []
    for simbolo, frecuencia in codigos.items():
        heappush(heap, (frecuencia, Nodo(simbolo)))

    while len(heap) > 1:
        frecuencia1, nodo1 = heappop(heap)
        frecuencia2, nodo2 = heappop(heap)
        heappush(heap, (frecuencia1 + frecuencia2, Nodo(None, nodo1, nodo2)))

    return heappop(heap)[1]

def decodificar(cadena, arbol):
    bits = iter(cadena)
    raiz = arbol
    mensaje = []
    for bit in bits:
        if bit == '0':
            raiz = raiz.izquierda
        else:
            raiz = raiz.derecha
        if raiz.valor is not None:
            mensaje.append(raiz.valor)
    return ''.join(mensaje)

codigos = {
    'A': '000',
    'B': '0010',
    'C': '0011',
    'D': '0100',
    'E': '0101',
    'G': '0110',
    'I': '0111',
    'L': '1000',
    'M': '1001',
    'N': '1010',
    'O': '1011',
    'P': '1100',
    'Q': '1101',
    'R': '1110',
    'S': '1111',
    ' ': '0000',
    ',': '00101'
}

arbol = construir_arbol(codigos)
cadena = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
print(decodificar(cadena, arbol))

