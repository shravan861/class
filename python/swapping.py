a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(f"before swap\n a:{a}\n b:{b}\n c:{c}\n")
d=a
a=c
c=b
b=d
print(f"after swap\n a:{a}\t b:{b}\t c:{c}\t")