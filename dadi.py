'''
Imperative version of a simple dice game
'''

from random import random

def lancia(tipo_lancio):
    if tipo_lancio.lower() == 'equo':
        return lancio_equo()
    elif tipo_lancio.lower() == 'baro':
        return lancio_baro()

def lancio_baro():
    lancio = [int(1+random()*6),0]
    baro = int(random()*10)
    if baro >= 5:
        lancio[1] = lancio[0]
    else:
        valori_d2 = [i for i in range(1,7) if i != lancio[0]]
        lancio[1] = valori_d2[baro]
    return lancio

def lancio_equo():
    return [int(1+random()*6),int(1+random()*6)]

def esito(lancio):
    return lancio[0] == lancio[1]

def gioca():
    scelta = input('Che tipo di lancio vuoi eseguire?\nScrivi equo o baro. Esci per uscire:\n')
    while scelta.lower() != 'esci':
        while scelta.lower() != 'baro' and scelta.lower() != 'equo':
            scelta = input('Che tipo di lancio vuoi eseguire?\nScrivi equo o baro. Esci per uscire:\n')
        lancio = lancia(scelta)
        print(lancio)
        if esito(lancio):
            print('Hai vinto!!')
        else:
            print('Hai perso!!')
        scelta = input('Che tipo di lancio vuoi eseguire?\nScrivi equo o baro. Esci per uscire:\n')

"""
METODI DI TEST
def test_equo(): # testa la correttezza del lancio equo
    for i in range(1000):
        test = lancia('equo')
        if(test[0] < 1 or test[0] > 6 or test[1]<1 or test[1]>6):
            print("ERRORE:",test)
            break
    else:
        print('OK')

def test_baro(): # testa la correttezza del lancio baro
    for i in range(1000):
        test = lancia('baro')
        if(test[0] < 1 or test[0] > 6 or test[1]<1 or test[1]>6):
            print("ERRORE:",test)
            break
    else:
        print('OK')

def test_perc_baro(): # testa la randomicità del lancio baro
    v = 0
    for i in range(100000):
        if esito(lancio('baro')):
            v += 1
    print(v/1000,'%')

def test_perc_equo(): # testa la randomicità del lancio equo
    v = 0
    for i in range(100000):
        if esito(lancio('equo')):
            v += 1
    print(v/1000,'%')
"""

gioca()
