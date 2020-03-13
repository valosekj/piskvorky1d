from ai import tah_pocitace

# Funkce pro zapsani symbolu hrace (x) na danou pozici
def tah_hrace(retezec,symbol_hrac):

    # Smycka pro zadani pozice
    while True:
        try:
            cislo_pole = int(input('Jsi na tahu. Zadej cislo pole (0-{}): '.format(len(retezec)-1)))
        except ValueError:      # kontrola zda bylo zadano opravdu cislo
            print('Nezadal jsi cislo, zkus to znova: ')
        else:
            if cislo_pole >= 0 and cislo_pole <= len(retezec)-1:
                if retezec[cislo_pole] != '-':
                    print('Toto pole je již obsazeno, zkus to znova.')
                else:
                    break
            else:
                print('Cislo mimo rozsah, zkus to znova: ')

    retezec = retezec[:cislo_pole] + symbol_hrac + retezec[cislo_pole + 1:]
    return retezec

# Funkce pro vyhodnoceni znaku v retezci, volá funkci stav_hry
def vyhodnot(retezec):
    if 'xxx' in retezec:
        stav = 'x'
    elif 'ooo' in retezec:
        stav = 'o'
    elif '-' not in retezec:
        stav = '!'
    else:
        stav = '-'

    stav_hry(stav)

# Funcke pro vyhodnoceni stavu hry, hru ukonci, kdyz se dosahne tri stejnych znaku vedle sebe
def stav_hry(stav):
    if stav == '!':
        print('Doslo misto. Remiza.')
        exit()
    elif stav == 'x':
        print('Vyhral jsi!')
        exit()
    elif stav == 'o':
        print('Prohral jsi!')
        exit()

# Funkce která stridave vola tah_hrace a tah_pocitace
def piskvorky1d():

    delka_pole = 10
    if delka_pole <= 0:
        print('Delka pole je < 0. Hra nemuze zacit.')
        exit()

    retezec = '-' * delka_pole

    symbol_pocitace = 'o'
    symbol_hrac = 'x'

    print(retezec)

    while True:
        retezec = tah_hrace(retezec,symbol_hrac)
        print(retezec)
        vyhodnot(retezec)
        retezec = tah_pocitace(retezec,symbol_pocitace)
        print('PC zahral:')
        print(retezec)
        vyhodnot(retezec)

#piskvorky1d()