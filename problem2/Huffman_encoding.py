from __future__ import annotations
from queue import PriorityQueue
from dataclasses import dataclass, field

@dataclass(order=True)
class huffman_node:
    frequency: int
    letter: chr=field(compare=False)
    left: huffman_node = field(compare=False)
    right: huffman_node = field(compare=False)

"""liczy ilosc wystapien kazdej litery z alfabetu"""
def get_frequency(alphabet, text):
    frequency_table = {letter : 0 for letter in alphabet}

    for letter in text:
        frequency_table[letter] += 1
    
    q = PriorityQueue()

    for letter in frequency_table.keys():
        item = huffman_node(frequency_table[letter], letter, None, None)
        q.put(item)

    return q

"""tworzy drzewo Huffmana"""
def encode_huffman_tree(alphabet, text):
    q = get_frequency(alphabet, text)

    for i in range(len(alphabet) - 1):
        x = q.get()
        y = q.get()
        z = huffman_node(x.frequency + y.frequency, None, x, y)
        q.put(z)
    
    return q.get()

"""zwraca slownik kodow odpowiednich znakow"""
def get_codes(tree, code, codes):
    if (tree.letter != None):
        codes[tree.letter] = code
        return
    
    get_codes(tree.left, code + "0", codes)
    get_codes(tree.right, code + "1", codes)

"""kompresuje wiadomosc"""
def compress_message(message, codes):
    encoded_message = ""

    for letter in message:
        encoded_message += codes[letter]
    
    return encoded_message

"""odkodowuje zapisana skompresowana wiadomosc"""
def decompress_message(encoded_message, tree):
    decoded_message = ""
    current_node = tree

    for bit in encoded_message:
        if (int(bit) == 1):
            current_node = current_node.right
        else:
            current_node = current_node.left
        
        if (current_node.letter != None):
            decoded_message += current_node.letter
            current_node = tree
    
    return decoded_message

if __name__ == "__main__":
    text = ""
    text += 45 * 'a'
    text += 13 * 'b'
    text += 12 * 'c'
    text += 16 * 'd'
    text += 5 * 'f'
    text += 9 * 'e'

    q = get_frequency(set(text), text)

    while (not q.empty()):
        w = q.get()
        print(w.frequency, w.letter)
    
    codes = {}
    w = encode_huffman_tree(set(text), text)
    get_codes(w, "", codes)
    print(codes)
    print(text)
    encoded_message = compress_message(text, codes)
    print(encoded_message)
    decoded_message = decompress_message(encoded_message, w)
    print(decoded_message)