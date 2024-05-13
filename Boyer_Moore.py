def create_last(alphabet, template):
    last = {x:0 for x in alphabet}
    
    for i, letter in enumerate(template):
        last[letter] = i

    return last

def create_bmnext(pattern):
    pattern_length = len(pattern)
    bmnext = [0 for x in range(pattern_length + 1)]
    pi = [0 for x in range(pattern_length + 1)]
    i = pattern_length
    b = pattern_length + 1
    pi[i] = b

    while (i > 0):
        while ((b <= pattern_length) and (pattern[i - 1] != pattern[b - 1])):
            if bmnext[b] == 0:
                bmnext[b] = b - i

            b = pi[b]
        
        b -= 1
        i -= 1
        pi[i] = b
    
    b = pi[0]
    for i in range(pattern_length + 1):
        if (bmnext[i] == 0):
            bmnext[i] = b
        
        if (i == b):
            b = pi[b]
        
    return bmnext

def bm_search(text, pattern, alphabet):
    return_table = []
    last = create_last(alphabet, pattern)
    bmnext = create_bmnext(pattern)
    text_len = len(text)
    pattern_len = len(pattern)
    pp = -1
    i = 0

    while (i <= text_len - pattern_len):
        j = pattern_len - 1

        while (j > -1) and (pattern[j] == text[i + j]):
            j -= 1
        
        if (j == -1):
            pp = i
            return_table.append(i)
            i += bmnext[0]
        else:
            i += max(bmnext[j + 1], j - last[text[i + j]])
        
    return return_table

if (__name__ == "__main__"):
    print(bm_search("ABCDBABCABBCDABCAB", "ABCAB", ['A', 'B', 'C', 'D']))
    print(bm_search("AABBABABAAAABBBABBAABABAABBBBBAABBAAAABABAABBABBBBBABBABBBABABBBABAABBBAABBABBA", "BABAA", ['A', 'B']))