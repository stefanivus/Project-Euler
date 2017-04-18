def factorial(n):
    prod = 1
    while n > 1:
        prod *= n
        n -= 1
    return prod

def is_curious(n):
    string = list(str(n))
    arr = []
    for i in string:
        arr.append(int(i))
    suma = 0
    for i in arr:
        suma += factorial(i)
    if suma == n:
        return True
    else:
        return False

def find_curious_nums(limit):
    arr = []
    for i in range(limit):
        if is_curious(i):
            arr.append(i)
    return arr

def suma(arr):
    suma = 0
    for i in arr:
        if i != 1 and i != 2:
            suma += i
    return suma

print(suma(find_curious_nums(1000000)))



