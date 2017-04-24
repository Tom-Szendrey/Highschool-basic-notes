amount = int(input("How many blocks do you want, note much be more than 1 "))
x = 0
block = []
while amount >= x:
    block.append("*"*(1+x))
    x += 1

x = 0
while amount > x:
    print block[x]
    x += 1


    

