rows=5
for i in range(rows):
    if i%2==0:
        print("*"*rows)
    else:
        print(" " + " ".join(str(i+1) for_in range(rows)))    