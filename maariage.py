from math import sin
from random import randint
boys = ["ali", "reza", "farhad", "yasin", "benyamin",
        "mehrdad", "sajjad", "aydin", "asad", "fardin"]
girls = ["sara", "elham", "negar", "2fateme", "fatane",
         "elnaz", "mahsa", "mahtab", "niaz", "negin"]

marriag = []
_girls = []
_boys = []


w = int(len(girls))

while len(_girls) != w:
    M_randdom = randint(0, 9)
    W_random = randint(0, 9)
    boys_marriage = boys[M_randdom]
    girls_marriage = girls[W_random]
    if boys_marriage not in _boys:
        _boys.append(boys[M_randdom])

    if girls_marriage not in _girls:
        _girls.append(girls[W_random])

for i in range(0, 9):
    print('(', _girls[i], 'married with', _boys[i], ')', end=' ')

print(marriag)
