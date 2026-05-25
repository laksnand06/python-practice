n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total = total + i
for i in range(1, n + 1):
    if i < n:
        print(i, end=" + ")
    else:
        print(i, end=" ")
print("=", total)