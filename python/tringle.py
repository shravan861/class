n=int(input("n: "))
val=ord("Z")
for i in range(n):
    for j in range(n):
        if i==0:
            print(chr(val),end=" ")
        else:
            print("  ",end=" ")
    print()                 
