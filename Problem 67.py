



def find_max_sum(arr1):
    first = arr1[len(arr1)-1]
    for i in range(len(arr1)-1,0,-1):
        second = arr1[i-1]
        for j in range(len(second)):
            if first[j] >= first[j+1]:
                second[j] += first[j]
            else:
                second[j] += first[j+1]
        first = second
    return first

print(find_max_sum(arr1))
