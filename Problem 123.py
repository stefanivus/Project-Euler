def find_primes(limit):
    arr = []
    for i in range(1,limit):
        arr.append(i+1)
    for i in arr:
        count = 2
        while count*i <= limit:
            if count*i in arr:
                del arr[arr.index(count*i)]
            count += 1
    return arr

print(find_primes(1000))
