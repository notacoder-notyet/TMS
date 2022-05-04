a, b, c = (1, 2), (1, 2), (1, 2)
print(id(a), id(b), id(c))
print(a, b, c) # 3 переменных с одинаковыми данными и идентификаторами
print(type(a), type(b), type(c))

d = 1
e = float(d)
print(id(d), id(e))
print(d, e)
print(type(d), type(e)) # 2 переменные с одинаковыми данными, но разными идентификаторами

aV2, bV2, cV2 = list(a), list(b), list(c)
print(id(aV2), id(bV2), id(cV2))
print(aV2, bV2, cV2)
print(type(aV2), type(bV2), type(cV2)) # Первые три разные id

eV2 = int(e)
print(id(d), id(eV2))
print(d, eV2)
print(type(d), type(eV2))



