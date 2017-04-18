import math
def factorial(x):
	result = 1
	for i in range(x,1,-1):
		result *= i
	return result

def find(x, arr):
    final_arr = []
    x = x-1
    i = 1
    while x > 0:
        fact_num = factorial(len(arr)-1)
        number = math.floor(x/fact_num)
        x %= fact_num
        final_arr.append(str(arr[number]))
        del arr[number]
    final_arr.append(str(arr[0]))
    result = "".join(final_arr)
    return result

x = 1000000
arr = [0,1,2,3,4,5,6,7,8,9]

print(find(x,arr))
