from __future__ import annotations
from queue import PriorityQueue
from dataclasses import dataclass, field

@dataclass(order=True)
class huffman_node:
    frequency: int
    letter: chr=field(compare=False)
    left: huffman_node = field(compare=False)
    right: huffman_node = field(compare=False)


def get_frequency(alphabet, text):
    frequency_table = {letter : 0 for letter in alphabet}

    for letter in text:
        frequency_table[letter] += 1
    
    q = PriorityQueue()

    for letter in frequency_table.keys():
        item = huffman_node(frequency_table[letter], letter, None, None)
        q.put(item)

    return q

def encode_huffman_tree(alphabet, text):
    q = get_frequency(alphabet, text)

    for i in range(len(alphabet) - 1):
        x = q.get()
        y = q.get()
        z = huffman_node(x.frequency + y.frequency, None, x, y)
        q.put(z)
    
    return q.get()

def get_codes(tree, code, codes):
    if (tree.letter != None):
        codes.append((tree.letter, code))
        return
    
    get_codes(tree.left, code + "0", codes)
    get_codes(tree.right, code + "1", codes)


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
    
    codes = []
    w = encode_huffman_tree(set(text), text)
    get_codes(w, "", codes)
    print(codes)