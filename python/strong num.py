def strong_num(n):
    temp=n
    sum=0
    while n>0:
        res=n%10
        fact=1
        for i in range(1,res+1):
            fact*=1
            sum+=fact
            n//=10
        return temp==sum 
print(strong_num(145)) 
print(strong_num(23))      