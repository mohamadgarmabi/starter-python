n = int(input("Enter the number of rows: "))
x = int(input("Enter the number of columns: "))

for _ in range(m):
    if x % 2 == 1:
        x = x * 2 - 1
    else:
        x = x // 2 
print(f"x is {x}")