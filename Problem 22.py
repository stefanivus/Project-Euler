path = "files/names.txt"

alphabet = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
def transform(path):
    string = ""
    file = open(path, "r")
    for line in file.readlines():
        string += line
    file.close()
    arr = string.split(",")
    for i in range(len(arr)):
        arr[i] = arr[i][1:len(arr[i])-1]
    return arr
    
def name_value(name):
    name = list(name)
    suma = 0
    for i in range(len(name)):
        suma += int(alphabet[name[i].lower()])
    return suma

def total_score(arr):
    suma = 0
    arr = sorted(arr)
    for i in range(len(arr)):
        suma += name_value(arr[i])*(i+1)
    return suma
    
print(total_score(transform(path)))
