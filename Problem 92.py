def number_chain(n):
    end_num = n
    while True:
        tmp = str(end_num)
        tmp = list(tmp)
        end = 0
        for i in range(0,len(tmp)):
            tmp[i] = int(tmp[i])*int(tmp[i])
            end += tmp[i]
        if end == 1 or end == 89:
            return end
        else:
            end_num = end
        
count = 0
for i in range(1,10000000):
    if number_chain(i) == 89:
        count += 1
print("Finished:",count)
