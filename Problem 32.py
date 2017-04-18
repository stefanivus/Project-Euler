nums = "123456789"

def size(n):
    n = len(str(n))
    return n

def find_pan():
    arr = []
    for i in range(1,5000000):
        j = i
        if size(i)+size(j)+size(i*j) > 9:
            break
        while size(i)+size(j)+size(i*j) <= 9:
            tmp_arr = [i,j,i*j]
            string = str(i)+str(j)+str(i*j)
            string = sorted(list(string))
            string = "".join(string)
            if string == nums:
                arr.append(i*j)
            j += 1
    return arr

def make_unique(arr):
    size = len(arr)
    arr2 = []
    for i in range(size):
        check = True
        for j in arr2:
            if j == max(arr):
                check = False
        if check == True:
             arr2.append(max(arr))     
        del arr[arr.index(max(arr))]
    return arr2
        
def suma(arr):
    suma = 0
    for i in arr:
        suma += i
    return suma

print(suma(make_unique(find_pan())))
