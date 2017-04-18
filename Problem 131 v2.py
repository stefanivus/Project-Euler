import math

def is_prime(n):
    i = 2
    while i < math.ceil(math.sqrt(n))+1:
        if n%i == 0:
            return False
        if i == 2:
            i += 1
        else:
            i += 2
    return True

def is_cubed(n):
    k = n**(1.0/3.0)
    if int(round(k))**3 == n:
        return True
    else:
        return False

count = 0
for i in range(1,577):
    if is_prime((i+1)**3-i**3):
        count += 1

print(count)
