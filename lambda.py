from functools import reduce

def addd(a, b):
    return a + b

secti = lambda a, b: a + b

print(secti(5, 10))

print(addd(5, 10))

num = [1,2,3,4,5]

dvojnasobek = list(map(lambda x: x * 2, num))

print(dvojnasobek)

liche = list(filter(lambda x: x % 2 != 0, num))

print(liche)

soucet = reduce(lambda x, y: x + y, num)
print(sum(num))
print(soucet)

