import math
digits = "987654321"
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

def is_pandigital():
    arr = []
    
    
