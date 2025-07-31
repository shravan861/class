n=int(input("n:"))
val=n
for i in range (n):
    for j in range(n):
        if i<=j:
            print("*",end=" ")
    print() 
    val+=1   