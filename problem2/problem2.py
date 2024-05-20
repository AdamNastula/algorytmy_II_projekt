from Huffman_encoding import encode_huffman_tree, get_codes
from Boyer_Moore import bm_search

"""
wejscie: melodia, liczba naturalna okreslajaca ilosc elementow w alfabecie 
oraz alfabet uzyty do zapisu melodi, przykladowe wejscie:

polipoliAAAApoliBBBBXXXXCCCCWWWWpolipoli
9
p
o
l
i
A
B
X
C
W

wyjscie: dla kazdej litery w alfabecie jej kod Huffmana
         poprawiona melodia (zamienione poli na boli)
"""

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
codes = []
get_codes(tree, "", codes)
for code in codes:
    print(code[0], code[1])

print(fixed_melody)