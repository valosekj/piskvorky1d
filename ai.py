from random import randrange

# Funkce pro zapsani symbolu pocitace (o) na nahodnou pozici
def tah_pocitace(retezec,symbol_pocitace):

    # Smycka pro zadani pozice
    while True:
        cislo_pole = randrange(0,20)
        if retezec[cislo_pole] == '-':
            break

    retezec = retezec[:cislo_pole] + symbol_pocitace + retezec[cislo_pole + 1:]
    return retezec

