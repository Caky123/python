t = (1, 2, [3, 4])
t[2].append(5)

print(t)

# Je tuple neměnný? Jak můžeš upravit jeho obsah?

def pridej(prvek, seznam=[]):
    seznam.append(prvek)
    return seznam

print(pridej("kočka"))
print(pridej("pes"))

# Co se vytiskne?

x = 10

def zmen(cislo):
    cislo += 5
    return cislo

zmen(x)
print(x)



a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # ?
print(a is b)  # ?
