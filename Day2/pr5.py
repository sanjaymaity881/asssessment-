def check_number(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

# Example usage:
num = float(input("Enter a number: "))  # Accept a number from the user
result = check_number(num)              # Call the function to check the number
print("Result:", result)                # Print the result
