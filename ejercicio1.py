class HuffmanNode:
    def __init__(self, char, freq, izd=None, dcha=None):
        self.char = char
        self.freq = freq
        self.izd = izd
        self.dcha = dcha

    def __lt__(self, other):
        return self.freq < other.freq

    def construir_arbol_huffman(frecuencias):
        nodos = []
        for caracter, frecuencia in frecuencias.items():
            nodos.append(HuffmanNode(caracter, frecuencia))
        while len(nodos) > 1:
            nodos.sort(key=lambda x: x.freq)
            nodo_izd = nodos.pop(0)
            nodo_dcha = nodos.pop(0)
            nodo_padre = HuffmanNode(None, nodo_izd.freq + nodo_dcha.freq)
            nodo_padre.izd = nodo_izd
            nodo_padre.dcha = nodo_dcha
            nodos.append(nodo_padre)
        return nodos[0]

def decode_string(root, s):
    result = []
    curr = root
    for bit in s:
        if bit == '0':
            curr = curr.izd
        else:
            curr = curr.dcha
        if curr.char is not None:
            result.append(curr.char)
            curr = root
    return ''.join(result)

def espacio_ocupado(frecuencias, encoded):
    return len(frecuencias) * 8 + len(encoded)

def main():
    freq_map_1 = {'A': 0.098, 'B': 0.017, 'C': 0.035, 'D': 0.026, 'E': 0.125, 'G': 0.026, 'I': 0.053, 'L': 0.053, 'M': 0.026, 'N': 0.053, 'O': 0.062, 'P': 0.035, 'Q': 0.008, 'R': 0.08, 'S': 0.035, 'T': 0.026, 'U': 0.035, 'V': 0.017, ' ': 0.15, ',': 0.017}
    root_1 = HuffmanNode.construir_arbol_huffman(freq_map_1)
    encoded_1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
    decoded_1 = decode_string(root_1, encoded_1)
    print("Mensaje 1: ", decoded_1)
    print("Espacio ocupado: ", espacio_ocupado(freq_map_1, encoded_1), "bits")

    root_2 = HuffmanNode.construir_arbol_huffman(freq_map_1)
    encoded_2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
    decoded_2 = decode_string(root_2, encoded_2)
    print("Mensaje 2: ", decoded_2)
    print("Espacio ocupado: ", espacio_ocupado(freq_map_1, encoded_2), "bits")
          
if __name__ == "__main__":
    main()