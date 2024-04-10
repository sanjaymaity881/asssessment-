rows = 5

for i in range(rows, 0, -1):
    # Print '*' i times in each row
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after printing each row
