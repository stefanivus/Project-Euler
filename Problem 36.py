def invert(n):
    arr = list(str(n))
    arr2 = []
    for i in range(len(arr)-1,-1,-1):
        arr2.append(arr[i])
    n2 = int("".join(arr2))
    return n2

def to_binary(n):
    binary_n = []
    while n > 0:
        binary_n.append(str(n%2))
        n = int(n/2)
    tmp_arr = []
    for i in range(len(binary_n)-1,-1,-1):
        tmp_arr.append(binary_n[i])
    binary_n = int("".join(tmp_arr))
    return binary_n

def find_palin(limit):
    arr = []
    for i in range(1,limit):
        if invert(i) == i:
            bin_i = to_binary(i)
            if bin_i == invert(bin_i):
                arr.append(i)
    return arr

def suma(arr):
    suma = 0
    for i in arr:
        suma += i
    return suma

print(suma(find_palin(1000000)))
