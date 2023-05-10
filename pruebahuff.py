import heapq

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, parent)
    return heap[0]

def decode_string(root, s):
    result = []
    curr = root
    for bit in s:
        if bit == '0':
            curr = curr.left
        else:
            curr = curr.right
        if curr.char is not None:
            result.append(curr.char)
            curr = root
    return ''.join(result)

# Example usage
freq_map = {'A':11, 'B':2, 'C':4, 'D':3, 'E':14, 'G':3, 'I':6, 'L':6, 'M':3, 'N':6, 'O':7, 'P':4, 'Q':1, 'R':10, 'S':4, 'T':3, 'U':4, 'V':2, ' ':17, ',':2}
root = build_huffman_tree(freq_map)
encoded = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
decoded = decode_string(root, encoded)
print("Mensaje 1: ", decoded)
encoded_2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
decoded_2 = decode_string(root, encoded_2)
print("Mensaje 2: ", decoded_2)