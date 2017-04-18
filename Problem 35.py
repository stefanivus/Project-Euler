import math

def is_prime(n):
    if n == 2:
        return True
    elif n == 1:
        return False
    elif n == 3:
        return True
    elif n%2 == 0:
        return False
    for i in range(3,math.ceil(math.sqrt(n))+2,2):
        if n%i == 0:
            return False
    return True

def circulate(arr):
    arr2 = arr
    arr2.append(arr[0])
    del arr2[0]
    return arr2


def is_circular(n):
    size = len(str(n))
    for i in list(str(n)):
        if int(i)%2 == 0:
            return False
    for i in range(size):
         digits = list(str(n))
         digits = circulate(digits)
         n = int("".join(digits))
         if is_prime(n) == False:
             return False
    return True

def find_circular_primes(limit):
    arr = [2]
    for i in range(2,limit):
        if is_prime(i):
            if is_circular(i):
                arr.append(i)
    return arr

print(len(find_circular_primes(1000000)))
            
            


