arr = ["one","two","three","four","five","six","seven","eight","nine"]
arrh = ["","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hund = ["","onehundredand","twohundredand","threehundredand","fourhundredand","fivehundredand","sixhundredand","sevenhundredand","eighthundredand","ninehundredand"]
tens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
hund1 = ["","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred","sevenhundred","eighthundred","ninehundred"]
i = 0
string =""
while (i < len(hund)):
    j=0
    while (j < len(arrh)):
        k=0
        while (k < len(arr)):
            string += hund[i] + arrh[j] + arr[k]
            k += 1
        j += 1
    i += 1 

i=0
while (i < len(hund)):
    
    j=0
    while (j < len(tens)):
         string += hund[i] + tens[j]
         j += 1
    i += 1

i=0
arrh = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
while (i < len(hund)):
    
    j=0
    while (j < len(arrh)):
         string += hund[i] + arrh[j]
         print(hund[i] + arrh[j])
         j += 1
    i += 1
i=0
while (i < len(hund1)):
    string += hund1[i]
    i += 1

string += "onethousand"
print(len(string))


            
            
            
    
