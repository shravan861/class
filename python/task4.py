import math
class LogicalPrograms:
    def find_hcf(self):
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
        minimum = min(n1, n2)
        hcf = 1
        for i in range(1, minimum + 1):
            if n1 % i == 0 and n2 % i == 0:
                hcf = i
        print(f"HCF is {hcf}")
    
    def find_hcf_using_math(self):
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
        n3 = int(input("n3: "))
        print(f"HCF using math.gcd: {math.gcd(math.gcd(n1, n2), n3)}")
    
    def find_lcm(self):
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
        lcm = None
        m = max(n1, n2)
        temp = m
        while True:
            if m % n1 == 0 and m % n2 == 0:
                lcm = m
                break
            m += temp
        print(f"LCM is {lcm}")

    def check_palindrome(self):
        n = int(input("n: "))
        temp = n
        rev = 0
        while n > 0:
            rem = n % 10
            rev = rem + rev * 10
            n //= 10
        if temp == rev:
            print("Palindrome")
        else:
            print("Not a Palindrome")
    
    def decimal_to_binary(self):
        n = int(input("Decimal number: "))
        bi = 0
        pos = 1
        while n > 0:
            rem = n % 2
            bi = bi + rem * pos
            n //= 2
            pos *= 10
        print(f"Binary form: {bi}")

    def binary_to_decimal(self):
        n = int(input("Binary number: "))
        dec = 0
        pow = 0
        while n > 0:
            rem = n % 10
            dec = dec + rem * (2 ** pow)
            pow += 1
            n //= 10
        print(f"Decimal form: {dec}")

    def decimal_to_octal(self):
        n = int(input("Decimal number: "))
        print(f"Octal form: {oct(n)[2:]}")

    def octal_to_decimal(self):
        n = input("Octal number: ")
        print(f"Decimal form: {int(n, 8)}")

    def decimal_to_hexadecimal(self):
        n = int(input("Decimal number: "))
        print(f"Hexadecimal form: {hex(n)[2:].upper()}")

    def decimal_to_roman(self):
        n = int(input("Decimal number: "))
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        i = 0
        while n > 0:
            for _ in range(n // val[i]):
                roman += syb[i]
                n -= val[i]
            i += 1
        print(f"Roman numeral: {roman}")

    def check_armstrong(self):
        n = int(input("n: "))
        temp = n
        p = len(str(n))
        res = 0
        while temp > 0:
            rem = temp % 10
            res += rem ** p
            temp //= 10
        if res == n:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")

    def check_perfect(self):
        n = int(input("n: "))
        var = 0
        for i in range(1, n):
            if n % i == 0:
                var += i
        if var == n:
            print("Perfect number")
        else:
            print("Not a Perfect number")

    def check_special(self):
        n = int(input("n: "))
        temp = n
        sum_, p = 0, 1
        while temp > 0:
            rem = temp % 10
            sum_ += rem
            p *= rem
            temp //= 10
        if sum_ + p == n:
            print("Special number")
        else:
            print("Not a Special number")

    def check_strong_number(self):
        n = int(input("n: "))
        temp = n
        sum_ = 0
        while n > 0:
            rem = n % 10
            fact = 1
            for i in range(1, rem + 1):
                fact *= i
            sum_ += fact
            n //= 10
        if sum_ == temp:
            print("Strong number")
        else:
            print("Not a Strong number")

    def check_spy_number(self):
        n = int(input("n: "))
        sum_, pro = 0, 1
        while n > 0:
            rem = n % 10
            sum_ += rem
            pro *= rem
            n //= 10
        if sum_ == pro:
            print("Spy number")
        else:
            print("Not a Spy number")

    def check_buzz_number(self):
        n = int(input("n: "))
        if n % 7 == 0 or str(n).endswith('7'):
            print("Buzz number")
        else:
            print("Not a Buzz number")


obj_L =LogicalPrograms()
obj_L.octal_to_decimal()
obj_L.binary_to_decimal()
obj_L.check_armstrong()
obj_L.check_buzz_number()
obj_L.check_perfect()
obj_L.check_special()
obj_L.check_spy_number()
obj_L.check_strong_number()
obj_L.decimal_to_binary()
obj_L.decimal_to_hexadecimal()
obj_L.decimal_to_octal()
obj_L.decimal_to_roman()
obj_L.find_hcf()
obj_L.find_lcm()