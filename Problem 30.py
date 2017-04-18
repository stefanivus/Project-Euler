def stringify(n):
    tmp_n = list(str(n))
    for i in range(len(tmp_n)):
        tmp_n[i] = int(tmp_n[i])
    return tmp_n

def power_sum(n, e):
    suma = 0
    for i in n:
         suma += i**e
    return suma

def F(n):
    arr = []
    for i in range(2,n):
        a = stringify(i)
        if power_sum(a, 5) == i:
            arr.append(i)
    return arr

def sum_array(n):
    suma = 0
    for i in n:
        suma += i
    return suma

a = F(999999)
print(a)
print(sum_array(a))
          
