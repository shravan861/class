class Patterns:
    def right_angle_triangle(self):
        n = int(input("n: "))
        val = ord("Z")
        for i in range(n):
            for j in range(n):
                if i + j >= n - 1:
                    print(chr(val), end=" ")
                    val -= 1
                else:
                    print(" ", end=" ")
            print()

    def diagonal(self):
        n = int(input("n: "))
        val = ord("Z")
        for i in range(n):
            for j in range(n):
                if i + j == n - 1:
                    print(chr(val), end=" ")
                    val -= 1
                else:
                    print(" ", end=" ")
            print()

    def diagonal_from_A(self):
        n = int(input("n: "))
        val = ord("A") + n - 1
        for i in range(n):
            for j in range(n):
                if i + j == n - 1:
                    print(chr(val), end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def right_triangle_numbers(self):
        n = int(input("n: "))
        val = n
        for i in range(n):
            for j in range(n):
                if i + j >= n - 1:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def left_triangle_numbers(self):
        n = int(input("n: "))
        val = n
        for i in range(n):
            for j in range(n):
                if i + j <= n - 1:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def left_triangle_characters(self):
        n = int(input("n: "))
        val = ord("D")
        for i in range(n):
            for j in range(n):
                if i + j <= n - 1:
                    print(chr(val), end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def left_triangle_Z(self):
        n = int(input("n: "))
        val = ord("Z")
        for i in range(n):
            for j in range(n):
                if i + j <= n - 1:
                    print(chr(val), end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def diagonal_numbers(self):
        n = int(input("n: "))
        val = n
        for i in range(n):
            for j in range(n):
                if i + j == n - 1:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def diagonal_special(self):
        n = int(input("n: "))
        val = n + n + 1
        for i in range(n):
            for j in range(n):
                if i + j == n - 1:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def increasing_line(self):
        n = int(input("n: "))
        val = 1
        for i in range(n):
            for j in range(n):
                print(" ", end=" ")
            for k in range(n):
                print(val, end=" ")
                val += 1
            val -= 2
            print()

    def pattern1(self):
        n = int(input("n: "))
        val = ord("Z")
        for i in range(n):
            for j in range(n):
                if (i + j) >= n - 1:
                    print(chr(val), end=" ")
                else:
                    print(" ", end=" ")
            print()
            val -= 1

    def pattern2(self):
        n = int(input("n: "))
        val = ord("z")
        for i in range(n):
            for j in range(n):
                if (i + j) == n - 1:
                    print(chr(val), end=" ")
                else:
                    print(" ", end=" ")
            print()
            val -= 1

    def pattern3(self):
        n = int(input("n: "))
        for i in range(n):
            val = ord("A")
            for j in range(n):
                if (i + j) == n - 1:
                    print(chr(val), end=" ")
                    val += 1
                else:
                    print(" ", end=" ")
            print()

    def pattern4(self):
        print("No code provided for pattern 4!")

    def pattern5(self):
        n = int(input("n: "))
        val = n
        for i in range(n):
            for j in range(n):
                if (i + j) <= n - 1:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def pattern6(self):
        n = int(input("n: "))
        val = ord("Z")
        for i in range(n):
            for j in range(n):
                if (i + j) <= n - 1:
                    print(chr(val), end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def pattern7(self):
        n = int(input("n: "))
        val = ord("A") + n - 1
        for i in range(n):
            for j in range(n):
                if (i + j) <= n - 1:
                    print(chr(val), end="")
                else:
                    print(" ", end="")
            val -= 1
            print()

    def pattern8(self):
        n = int(input("n: "))
        val = n
        for i in range(n):
            for j in range(n):
                if (i + j) == n - 1:
                    print(val, end=" ")
                else:
                    print(" ", end=" ")
            val -= 1
            print()

    def pattern9(self):
        n = int(input("n: "))
        for i in range(n):
            for j in range(n):
                if (i + j) >= n - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def pattern10(self):
        n = int(input("n: "))
        val = 1
        for i in range(n):
            for j in range(n):
                if (i + j) >= n - 1:
                    print(val, end=" ")
                    val += 1
                    if val > 9:
                        val = 1
                else:
                    print(" ", end=" ")
            print()

    def pattern11(self):
        n = int(input("n: "))
        for i in range(n):
            for j in range(n):
                if i == j:
                    print("* ", end=" ")
                elif (i + j) >= n - 1:
                    print("$ ", end=" ")
                else:
                    print("# ", end=" ")
            print()
object_p=Patterns()
object_p.diagonal()
object_p.diagonal_from_A()
object_p.diagonal_numbers()
object_p.diagonal_special()
object_p.increasing_line()
object_p.left_triangle_characters()
object_p.left_triangle_numbers()
object_p.left_triangle_Z()
object_p.right_angle_triangle()
object_p.right_triangle_numbers()
object_p.pattern1()
object_p.pattern2()
object_p.pattern3()
object_p.pattern4()
object_p.pattern5()
object_p.pattern6()
object_p.pattern7()
object_p.pattern8()
object_p.pattern9()
object_p.pattern10()
object_p.pattern11()