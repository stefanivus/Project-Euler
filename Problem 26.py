import decimal

def find_repeat(n):
    n = str(n)
    n = n.split(".")
    n = n[1]
    n = list(n)
    arr = []
    for i in n:
        check = True
        for j in range(len(arr)):
            if arr[j] == i:
                string = ""
                for b in n:
                    string += str(b)
                c = n[int(i):len(string)]
                if string == c:
                    check = False
                    k = "".join(arr)
                    return k
        if check == True:
            arr.append(i)
    k = "".join(arr)
    return k

def largest_repeat(d):
    size = 0
    largest = 0
    for i in range(2,d):
        k = find_repeat(decimal.Decimal(1)/decimal.Decimal(i))
        if len(k) > size:
            size = len(k)
            largest = i
    return largest


print(largest_repeat(1000))
