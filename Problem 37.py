import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True

def is_truncable(n):
    size = len(str(n))-1
    s = str(n)
    check = True
    for i in range(size):
        a1 = int(s[0:len(s)-(i+1)])
        a2 = int(s[i+1:len(s)])
        if not is_prime(a1) or not is_prime(a2):
            check = False
            break
    if check:
        return True
    else:
        return False
      
def primes():
    arr = [2,3,5,7]
    arr2 = []
    i = 11
    while len(arr2) < 11:
        check = True
        for prime in arr:
            if i%prime == 0:
                check = False
                break
        if check == True:
            arr.append(i)
            if is_truncable(i):
                arr2.append(i)
                
        i += 2
    return arr2

def suma(arr):
    suma = 0
    for i in arr:
        suma += i
    return suma

arr = primes()
print(suma(arr))
