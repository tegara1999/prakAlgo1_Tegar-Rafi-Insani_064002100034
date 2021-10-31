kok1 = input("please enter 4 character string = ")
kok2 = ''
 
for i in kok1:
    if ord(i) >= 90:
        i = chr(ord(i)-32)
    kok2 = kok2 + i
 

print("the string capitalization is " ,kok2)