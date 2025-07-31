n=int(input("n:"))
for i in range (n-1,-n-1):
    for j in range(n-abs(i)):
        print("*",end=" ")
    print()    