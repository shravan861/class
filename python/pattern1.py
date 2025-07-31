row=int(input("row:"))
col=int(input("col:"))
val=row
if val>9:
    val=9
for i in range(col):
    for j in range(row):
        print(val,end=" ")
    val-=1
    if val<1:
        val=9
    print()        