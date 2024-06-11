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


    ostatni=lines[0][2]
    indexOdwiedzonej=0
    nrWiezy=0
    piesni=0
    print("Postuj w w punkcie o indexie ", 0, " : ", lines[0][0],
          lines[0][1], "wartosc: ", lines[0][2])

    while nrWiezy < len(lines):
        indexOdwiedzonej=-1
        max=0
        for i in range(m):
                if nrWiezy + i < len(lines):
                    if (lines[nrWiezy + i][2]>max and lines[nrWiezy + i][2]<ostatni):
                        max=lines[nrWiezy + i][2]
                        #print("if 2 dane: ostatni: ", ostatni, " obecny: ", lines[j + i][2], " index: ", j + i)
                        indexOdwiedzonej = nrWiezy + i
        if indexOdwiedzonej==-1:
            for i in range(m):
                if nrWiezy + i < len(lines):
                    if lines[nrWiezy + i][2] > max:
                        max = lines[nrWiezy + i][2]
                        #print("if 3 dane: ostatni: ", ostatni, " obecny: ", lines[j + i][2], " index: ", j + i)
                        indexOdwiedzonej = nrWiezy + i
            ostatni=max
            print("Pieśń odsłuchana w punkcie o indexie:",indexOdwiedzonej," : ",lines[indexOdwiedzonej][0], lines[indexOdwiedzonej][1],"wartosc: ",lines[indexOdwiedzonej][2])
            ostatni = max
            piesni=piesni+1
            nrWiezy = indexOdwiedzonej + 1
        else:
            print("Postuj w w punkcie o indexie ",indexOdwiedzonej," : ", lines[indexOdwiedzonej][0], lines[indexOdwiedzonej][1],"wartosc: ",lines[indexOdwiedzonej][2])
            ostatni = max
            nrWiezy = indexOdwiedzonej + 1

    print()
    print("Odsłuchano pieśń: ",piesni," razy")
