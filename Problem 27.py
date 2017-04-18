import math

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n == 0:
        return False
    i = 2
    while i < math.ceil(math.sqrt(n))+1:
        if n%i == 0:
            return False
        if i == 2:
            i += 1
        else:
            i += 2
    return True


def find_quad(size):
    arr = [0,0,0]
    for a in range(-size,size):
        for b in range(-size+1, size+1):
            c = 3
            count = 0
            while is_prime(c) == True:
                c = abs(count**2 + count*a + b)
                count += 1
            if count-1 > arr[0]:
                arr[0] = count-1
                arr[1] = a
                arr[2] = b
    return arr
                        
arr = find_quad(1000)
print(arr)
