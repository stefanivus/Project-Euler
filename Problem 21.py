import math
def d(n):
    suma = 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            if i == n/i:
                suma += i
            else:
               suma += i + (n/i)
    return suma

suma = 0
for n in range(0,10000):
    if d(d(n)) == n and d(n) != n:
        suma += n

print(suma)
