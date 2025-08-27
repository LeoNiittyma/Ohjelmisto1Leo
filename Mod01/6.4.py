
def summa(lista):
    summa = sum(lista)
    return summa

def testaus():
    testilista1 = [1,2,3,4,5]
    testilista2 = [2,4,6,8,10]
    tulos1 = summa(testilista1)
    tulos2 = summa(testilista2)
    print(tulos1)
    print(tulos2)
    return

testaus()