n=int (input("n:"))
n=int(input("n:"))
val=1
P=True
for i in range(n):
    for j in range(n):
        if P:
            print(val,end=" ")
            P=False
            v+=1
        if val>9:
            val=1
        else:
            print("*",end=" ") 
            P=True
        print()           