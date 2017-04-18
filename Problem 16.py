i = 0
num = 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

while i < 1000:
    num *= 2
    i = i + 1



print(sum_digits(num));
