def create_spiral(size):
    arr = []
    for i in range(size):
        tmp_arr = []
        for j in range(size):
            tmp_arr.append(0)
        arr.append(tmp_arr)
    i = int(size/2)
    j = int(size/2) 
    step = 1
    step_count = 1
    count = 0
    for k in range(1,size**2+1):
        arr[j][i] = k
        if count == 0:
            i += 1
            if step_count >= step:
                count += 1
                step_count = 1
            else:
                step_count += 1
        elif count == 1:
            j += 1
            if step_count >= step:
                step += 1
                count += 1
                step_count = 1
            else:
                step_count += 1
        elif count == 2:
            i -= 1
            if step_count >= step:   
                count += 1
                step_count = 1
            else:
                step_count += 1
        elif count == 3:
            j -= 1
            if step_count >= step:
                count = 0
                step += 1
                step_count = 1
            else:
                step_count += 1
    return arr

def diagonal_sum(arr):
    suma = 0
    for i in range(len(arr)):
         suma += arr[i][i]
    j = 0
    for i in range(len(arr)-1,-1,-1):
            suma += arr[j][i]
            j += 1
    suma -= arr[int(len(arr)/2)][int(len(arr)/2)]
    return suma
    

arr = create_spiral(1001)
suma = diagonal_sum(arr)

print(suma)
        
        
    
