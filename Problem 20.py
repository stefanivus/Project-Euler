def factor(x):
    prod = 1
    while(x>1):
        prod *= x
        x -= 1
    return prod



total = 0
for digit in map(int, str(factor(100))):
    total += digit
print(total)
