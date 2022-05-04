print("Hello Oleg")
a = ((2 ** 5) * 2 - 16 * 2) / (8 ** 8)
print(a)
print('%.10f' % a)
typea = type(a)
aisint = type(a) is int
print(typea)
print(aisint)
b = [None, True, "Oleg", {"name": "Oleg"}, 1, 1.1, ["Oleg", 1], ("Oleg", 1), {1, 2, 3, 1, 1}]
typeb = type(b)
print(typeb)
