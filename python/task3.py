class pyramids:
 def pyramid_updown_numbers(self):
        n = int(input("n: "))
        val = 1
        for i in range(n):
            for j in range(n):
                if i >= j:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            val += 1
            print()
        for i in range(n - 1):
            for j in range(n - 1):
                if i + j <= n - 2:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

 def pyramid_updown_increase_numbers(self):
        n = int(input("n: "))
        for i in range(n):
            val = 1
            for j in range(n):
                if i >= j:
                    print(val, end=" ")
                    val += 1
                else:
                    print(" ", end=" ")
            print()
        for i in range(n - 1):
            val = n - 1
            for j in range(n - 1):
                if i + j <= n - 2:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            print()

 def pyramid_updown_decrease_numbers(self):
        n = int(input("n: "))
        for i in range(n):
            val = n
            for j in range(n):
                if i >= j:
                    print(val, end=" ")
                    val -= 1
                else:
                    print(" ", end=" ")
            print()
        for i in range(n - 1):
            val = n - 1
            for j in range(n - 1):
                if i + j <= n - 2:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            print()

 def pyramid_updown_increase_chars(self):
        n = int(input("n: "))
        val = ord('A')
        for i in range(n):
            for j in range(n):
                if i >= j:
                    print(chr(val), end=" ")
                else:
                    print(" ", end=" ")
            val += 1
            print()
        for i in range(n - 1):
            for j in range(n - 1):
                if i + j <= n - 2:
                    print(chr(val), end=" ")
                else:
                    print(" ", end=" ")
            val += 1
            print()

 def pyramid_updown_char_series(self):
        n = int(input("n: "))
        for i in range(n):
            val = ord('A')
            for j in range(n):
                if i >= j:
                    print(chr(val), end=" ")
                    val += 1
                else:
                    print(" ", end=" ")
            print()
        for i in range(n - 1):
            val = ord('A')
            for j in range(n - 1):
                if i + j <= n - 2:
                    print(chr(val), end=" ")
                    val += 1
                else:
                    print(" ", end=" ")
            print()
object_py=pyramids()
object_py.pyramid_updown_char_series()
object_py.pyramid_updown_decrease_numbers()
object_py.pyramid_updown_increase_chars()
object_py.pyramid_updown_increase_numbers()
object_py.pyramid_updown_numbers()