def read_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())

        lines = []

        for _ in range(n):
            line = file.readline().strip()
            # Podział linii na trzy liczby całkowite
            numbers = list(map(int, line.split()))
            lines.append(numbers)
        m = int(file.readline().strip())

    return lines, m

if __name__ == "__main__":
    filename = 'dane4.txt'  # nazwa pliku
    lines, m = read_file(filename)


    ostatni=0
    index=0
    j=0
    piesni=0
    while j < len(lines):
        index=-1
        max=0
        for i in range(m):
            if ostatni==0:
                if j+i<len(lines):
                    if lines[j+i][2]>max:
                        max=lines[j+i][2]
                        #print("if 1 dane: ostatni: ",ostatni," obecny: ",lines[j+i][2]," index: ",j+i)
                        index=j+i
            else:
                if j + i < len(lines):
                    if (lines[j+i][2]>max and lines[j+i][2]<ostatni):
                        max=lines[j+i][2]
                        #print("if 2 dane: ostatni: ", ostatni, " obecny: ", lines[j + i][2], " index: ", j + i)
                        index = j + i
        if index==-1:
            for i in range(m):
                if j + i < len(lines):
                    if lines[j + i][2] > max:
                        max = lines[j + i][2]
                        #print("if 3 dane: ostatni: ", ostatni, " obecny: ", lines[j + i][2], " index: ", j + i)
                        index = j + i
            ostatni=max
            print("Pieśń odsłuchana w punkcie o indexie:",index," : ",lines[index][0], lines[index][1])
            ostatni = max
            piesni=piesni+1
            j = index+1
        else:
            print("Postuj w w punkcie o indexie ",index," : ", lines[index][0], lines[index][1])
            ostatni = max
            j = index+1

    print()
    print("Odsłuchano pieśń: ",piesni," razy")
