def a_pow_b(start,end):
    arr = []
    for i in range(start,end+1):
        for j in range(start,end+1):
            arr.append(i**j)
    return arr

def sort_array(arr):
    size = len(arr)
    tmp_arr = []
    while len(tmp_arr) < size:
        tmp_arr.append(min(arr))
        del arr[arr.index(min(arr))]
    return tmp_arr

def remove_repeats(arr):
    size = len(arr)-1
    for i in range(size):
        if i+1 >= len(arr):
            break
        while arr[i] == arr[i+1]:
            del arr[i+1]
    return arr

def full(start,end):
    arr = a_pow_b(start,end)
    arr = sort_array(arr)
    arr = remove_repeats(arr)
    return arr
    
print(len(full(2,100)))



