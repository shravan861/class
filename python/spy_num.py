def spy_number(n):
    sum=0
    product=1
    while n>0:
        sum+=n%10
        product*=n%10
        n//=10
    return sum==product

print(spy_number(1124))
print(spy_number(345))    
        

