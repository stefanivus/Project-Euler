def rad(n):
    arr = []
    tmp_n = n
    i = 2
    tmp_i = 0
    while tmp_n > 1:
        if tmp_n%i == 0:
            tmp_n = tmp_n/i
            if tmp_i != i:
                arr.append(i)
                tmp_i = i
        else:
            i += 1
    prod = 1
    for k in arr:
        prod *= k
    return prod

def sort(arr):
    tmp_arr = [[],[]]
    size = len(arr[0])
    while len(tmp_arr[0]) < size:
       tmp_arr[0].append(min(arr[0]))
       tmp_arr[1].append(arr[1][arr[0].index(min(arr[0]))])
       del arr[1][arr[0].index(min(arr[0]))]
       del arr[0][arr[0].index(min(arr[0]))]
    return tmp_arr
    

def return_list(n_max):
    arr = [[],[]]
    for n in range(1,n_max+1):
        arr[0].append(rad(n))
        arr[1].append(n)
    arr = sort(arr)
    return arr

def E(k, arr):
    k -= 1
    return arr[1][k]

arr = return_list(100000)

print(E(10000,arr))
