import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # Define comparison operators for the heap based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

def build_huffman_tree(frequency):
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = Node(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_codes(root, current_code="", huffmancode={}):
    if root is None:
        return
    
    # Leaf node, store its code
    if root.char is not None:
        huffmancode[root.char] = current_code
    
    # Internal nodes
    build_huffman_codes(root.left, current_code + "0", huffmancode)
    build_huffman_codes(root.right, current_code + "1", huffmancode)

def generate_huffman_codes(text):
    frequency = build_frequency_table(text)
    root = build_huffman_tree(frequency)
    huffmancode = {}
    build_huffman_codes(root, "", huffmancode)
    
    return huffmancode

def compress_text(text, huffmancode):
    compressed = ""
    for char in text:
        compressed += huffmancode[char]
    return compressed

# Example usage
text = "this is an example for huffman coding"
huffmancode = generate_huffman_codes(text)
compressed_text = compress_text(text, huffmancode)

print("Original Text:", text)
print("Huffman Codes:", huffmancode)
print("Compressed Text:", compressed_text)
