from problem2.Huffman_encoding import encode_huffman_tree, get_codes, compress_message, decompress_message
from problem2.Boyer_Moore import bm_search
from problem2.Hamming_codes import encode_message

melody = input()
list_melody = list(melody)
n = input()
alphabet = []

for i in range(int(n)):
    alphabet.append(input())

poli_occurances = bm_search(melody, "poli", alphabet)

for occurance in poli_occurances:
    list_melody[occurance] = 'b'

fixed_melody = ""

for letter in list_melody:
    fixed_melody += letter

if ('b' not in alphabet):
    alphabet.append('b')

tree = encode_huffman_tree(alphabet, fixed_melody)
codes = {}
get_codes(tree, "", codes)

for letter, code in codes.items():
    print(letter, code)

print(fixed_melody)
compressed_message = compress_message(fixed_melody, codes)
print(compressed_message)
print(decompress_message(compressed_message, tree))
print(len(poli_occurances))
print(encode_message(compressed_message))