def parilliset(lista):
    parilista = []
    for luku in lista:
        if luku % 2 == 0:
            parilista.append(luku)
    return parilista

def testaus():
    testilista1 = [1,2,3,4,5,6,7,8,9,10]
    testilista2 = [10,11,13,16,20,25,31,38,46,55,65]
    tulos1 = parilliset(testilista1)
    tulos2 = parilliset(testilista2)
    print(tulos1)
    print(tulos2)
    return

testaus()