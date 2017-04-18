def R(k):
    end = "1"
    count = 0
    while len(end) != k:
        a = str(end)
        while len(end+a) > k:
            size = int(len(a)/2)
            a = a[0:size]
        end += a
        count += 1
    print(count)
    return int(end)

def prime_factors(n):
    tmp_n = n
    i = 0


R(10**8)
