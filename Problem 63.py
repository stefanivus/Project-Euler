n = [0,1,2,3,4,5,6,7,8,9]
def check(x,e):
    if len(str(x**e)) == e:
        return True
    else:
        return False

check1 = False
count = 0
for e in range(1,22):
    for i in range(0,len(n)):
        if check1 == True:
            i = i - 1
        if check(n[i],e) == True:
            count += 1
            print("yes", n[i], "^", e)
            check1 = False
        else:
            del n[i]
            print("no", n[i], "^", e)
            check1 = True
            
print(count)
