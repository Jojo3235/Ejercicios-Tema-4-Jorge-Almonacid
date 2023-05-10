# A Huffman Tree Node
import heapq
 
 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (character)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''
 
    def __lt__(self, nxt):
        return self.freq < nxt.freq
 
 
# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def printNodes(node, val=''):
 
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
 
def decoder(cadena, arbol):
    bits = iter(cadena)
    raiz = arbol
    mensaje = []
    for bit in bits:
        if bit == '0':
            raiz = raiz.left
        else:
            raiz = raiz.right
        if raiz.symbol is not None:
            mensaje.append(raiz.symbol)
            raiz = arbol

    return ''.join(mensaje)

def main():
    # cadena = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
    cadena = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
    # characters for huffman tree
    chars = ['A', 'B', 'C', 'D', 'E', 'G', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', ' ', ',']
    
    # frequency of characters
    freq = [11, 2, 4, 3, 14, 3, 6, 6, 3, 6, 7, 4, 1, 10, 4, 17, 2]
    
    # list containing unused nodes
    nodes = []
    
    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        heapq.heappush(nodes, node(freq[x], chars[x]))
    
    while len(nodes) > 1:
    
        # sort all the nodes in ascending order
        # based on their frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
    
        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1
    
        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    
        heapq.heappush(nodes, newNode)
    
    # Huffman Tree is ready!
    printNodes(nodes[0])
    print(decoder(cadena, nodes[0]))

if __name__ == "__main__":
    main()