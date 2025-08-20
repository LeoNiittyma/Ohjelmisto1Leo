leiviska_str = input("Anna leiviskät: ")
naula_str = input("Anna naulat: ")
luoti_str = input("Anna luodit: ")

leiviska = float(leiviska_str)
naula = float(naula_str)
luoti = float(luoti_str)

leiviskapaino = (leiviska * 13.3 * 20 * 32)
naulapaino = (naula * 13.3 * 32)
luotipaino = (luoti * 13.3)

yhteispaino = (leiviskapaino + naulapaino + luotipaino)

kg = yhteispaino // 1000
g1 = yhteispaino % 1000
g = g1 // 1

print("Massa nykymittojen mukaan:",kg,"kg ja",g,"grammaa.")