def digits(n):
    n = str(n)
    return len(n)

x = 0
x2 = 1
count = 0

while digits(x) < 1000:
    suma = x + x2
    x = x2
    x2 = suma
    count += 1

print(count)
    
