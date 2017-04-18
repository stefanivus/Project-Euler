import math
def find_prime_factors(n):
    factors = []
    i = 3
    while n > 1:
        if n%2 == 0:
            factors.append(2)
            n = n/2
        elif n%i == 0:
            factors.append(i)
            n = n/i
        else:
            i += 2
    return factors

def make_unique(arr):
    arr2 = []
    size = len(arr)
    for i in range(size):
        check = True
        for j in arr2:
            if j == min(arr):
                check = False
        if check == True:
            arr2.append(min(arr))
        del arr[arr.index(min(arr))]
    return arr2

def rad(n):
    arr = find_prime_factors(n)
    arr = make_unique(arr)
    p = 1
    for prime in arr:
        p *= prime
    return p

def GCD(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def is_abc_hit(a,b,c):
    if GCD(a,b) == 1:
        if GCD(a,c) == 1:
            if GCD(b,c) == 1:
                if rad(a)*rad(b)*rad(c) < c:
                    return True
    return False

def find_sum_c(limit):
    suma = 0
    for c in range(3, limit):
        for b in range(2,c):
            for a in range(1,b):
                if a+b == c:
                    if is_abc_hit(a,b,c):
                        suma += c
                        print(a,b,c)
    return suma

print(find_sum_c(100))
