# def geomProg(a,b,c):
#     """a - число которое в гепрогресию
#     b - количество шагов в прогрессии
#     с - на сколько множим"""
#     for i in range(b):
#         yield a
#         a *= c
# test = geomProg(2, 10, 2)
# for i in test:
#     print(i)

import re
file = 'oleg@google.com'
regex = r"^([a-z0-9_-_!#%&'\"_`+/=?{}|~-]+\.)*[a-z0-9_-_!#%&'\"`+/=?{}|~]+@(([a-z0-9]+[\-_?]*[a-z0-9]+)*\.[a-z]{2,6}){0,63}$"
recheck = re.fullmatch(regex, file)
print(recheck)