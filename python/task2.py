class pattern1:
    def ptr_str(self):
        n=int(input("n:"))
        m=int(input("m:"))
        for i in range(n):
            print("* "*m)
    print()

    def ptr_val(self):
        row=int(input("row:"))
        col=int(input("col:"))
        val=1
        for i in range(row):
            for j in range(col):
                print(val,end=" ")
            
            print()  
            val+=1      
            if val>9:  
             val=1

    def row_val(self):
        row = int(input("row: "))
        col = int(input("col: "))

        for i in range(row):
            val = 1  
            for j in range(col):
                print(val, end=" ")
                val += 1 
            print()

    def ptr_val1(self):
        row=int(input("row:"))
        col=int(input("col:"))
        val=1
        for i in range(row):
            
            for j in range(col):
                print(val,end=" ")
                
            print()
            val+=1
            if val>9:
             val=1

    def ptr_val2(self):
        row=int(input("row:"))
        col=int(input("col:"))
        val=1
        for i in range(row):
            for j in range(col):
                print(val,end=" ")
            print()
            val+=1
            if val>9:
                val=1
    def ptr_val3(self):
        row=int(input("row:"))
        col=int(input("col:"))
        val=1
        for i in range(row):
            if val>9:
             val=1
            for j in range(col):
                print(val,end=" ")
            val+=1
            print()
            if val>9:
                val=1
        
    def ptr_alf(self):
        row=int(input("row:"))
        col=int(input("col:"))

        for i in range(row):
            for j in range(col):
                print(chr(90-j),end=" ")
            print()

    def num_str(self):
        row = int(input("row: "))
        col = int(input("col: "))
        val = 1
        for i in range(row):
            if i % 2 == 0:  
                for j in range(col):
                    print(val, end=" ")
                    val += 1
            else:  
                for j in range(col):
                    print("*", end=" ")
            print()  


    def val_str2(self):
        row=int(input("row:"))
        col=int(input("col:"))
        val=1 
        for i in range(row):
            for j in range(col):
                if i%2==0:
                    print(val,end=" ")
                    val+=1
                else:
                    print("*",end=" ")
            print()
            if i%2==0:
             val+=1
            if i > 9:
             val=1

    def val_str3(self):
        row=int(input("row:"))
        col=int(input("col:"))

        for i in range(row):
            val=1
            for j in range(col):
                if j%2 ==0:
                
                    print(val,end=" ")
                    val+=1
                else:
                    print("*",end=" ")
            print()
    def val_str4(self):
        row=int(input("row:"))
        col=int(input("col:"))

        for i in range(row):
            val=1
            for j in range(col):
                if j%2 ==0:
                
                    print(val,end=" ")
                    val+=1
                else:
                    print("*",end=" ")
            print()
    def alf_str(self):
        row=int(input("row:"))
        col=int(input("col:"))
        val=65
        for i in range(row):
            for j in range(col):
                if i%2==0:
                 print(chr(val),end=" ")
                else:
                 print("*",end=" ")
            print()
    def alf_str1(self):
        row=int(input("row:"))
        col=int(input("col:"))
        val=65
        for i in range(row):
            for j in range(col):
                if j%2==0:
                    print(chr(val),end=" ")
                    val+=1
                else:
                    print("*",end=" ")
            print() 
    def san(self):
        n=int(input("n:"))
        for i in range(n):
            val=1
            for j in range(n):
                if i>=j:
                    print(val,end=" ")
                    val+=1
                else:
                    print(" ",end=" ")  
            print() 

        print()


        n=int(input("n:"))
        val=1
        for i in range(n):
            
            for j in range(n):
                if i==j:
                    print(val,end=" ")
                    val+=1
                else:
                    print(" ",end=" ")  
            print() 

        print()

        n=int(input("n:"))
        for i in range(n):
            val=1
            for j in range(n):
                if i<=j:
                    print(val,end=" ")
                    val+=1
                else:
                    print(" ",end=" ")  
            print() 

        print()

        n=int(input("n:"))
        val=n
        for i in range(n):
            for j in range(n):
                if i==j:
                    print(val,end=" ")
                else:
                    print(" ",end=" ")  
            print() 
            val-=1
    def abc_pt(self):
        n=int(input("n:"))
        val=ord("A")
        for i in range(n):
            for j in range(n):
                if i==j:
                    print(chr(val),end=" ")
                    val+=1
                else:
                    print(" ",end=" ")  
                
            print() 

        n=int(input("n:"))
        val=ord("A")+n-1
        for i in range(n):
            for j in range(n):
                if i==j:
                    print(chr(val),end=" ")
                    val-=1
                
                else:
                    print(" ",end=" ")
            print() 

    def str_ptr1(self):
                
        n=int(input("n:"))
        for i in range(n):
            for j in range(n):
                if i==j:
                    print("*",end=" ")
                    
                else:
                    print(" ",end=" ")
            
            print() 

    def str_ptr1(self):    
        n=int(input("n:"))
        for i in range(n):
            for j in range(n):
                if i+j<=n-1:
                    print("*",end=" ")
                    
                else:
                    print(" ",end=" ")
            
            print() 


    def str_ptr2(self):    
        n=int(input("n:"))
        for i in range(n):
            for j in range(n):
                if i+j>=n-1:
                    print("*",end=" ")
                    
                else:
                    print(" ",end=" ")
            
            print() 

    def str_ptr3(self):
        n=int(input("n:"))
        val=1
        for i in range(n):
            for j in range(n):
                if i+j==n-1:
                    print(val,end=" ")
                    val+=1
                    
                else:
                    print(" ",end=" ")
            print() 
    def str_ptr4(self):
        n=int(input("n:"))
        val=ord("A")
        for i in range(n):
            for j in range(n):
                if (i+j)>=n-1:
                    print(chr(val),end=" ")
                    val+=1
                    
                else:
                    print(" ",end=" ")
            
            print() 



                    
       


obj=pattern1() 
obj.ptr_str()
obj.ptr_val() 
obj.row_val()
obj.ptr_val1()
obj.ptr_val2()
obj.ptr_val3()
obj.ptr_alf()
obj.num_str()
obj.val_str2()
obj.val_str3()
obj.val_str4()
obj.alf_str()
obj.alf_str1()
obj.san()
obj.abc_pt()
obj.str_ptr()
obj.alf_str1()
obj.alf_str2()
obj.val_str3()
obj.val_str3()
obj.val_str4()