def zad1():
    s = input()

    for i in range(len(s)):
        print("s[", i, "] = ", s[i], sep="")

def zad2():
    s = input()
    i = len(s) - 1

    while (i >= 0):
        print("s[", i, "] = ", s[i], sep="")
        i -= 1

def zad3():
    s = input()
    p = input()
    len_s = len(s)
    len_p = len(p)
    i = 0

    while (i <= len_s - len_p):
        if (s[i:i+len_p] == p):
            print(i)

        i += 1

"""Ja to rozumiem tak ze kazde wystapienie danej litery zastepuje innym znakiem"""
def zad4():
    s = input()
    zamieniany = input()
    zamieniajacy = input()

    if (len(zamieniany) != 1):
        print("Drugi argument musi byc pojedynczym znakiem!")
        return

    if (len(zamieniajacy) != 1):
        print("Trzeci argument musi byc pojedynczym znakiem!")
        return

    s = s.replace(zamieniany, zamieniajacy)

    print(s)            

if __name__ == "__main__":
    #zad1()
    #zad2()
    #zad3()
    zad4()