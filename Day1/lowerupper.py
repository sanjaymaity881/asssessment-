char = input("Enter a character: ")

if char.isalpha():
    if char.isupper():
        print("The entered character is an uppercase letter.")
    elif char.islower():
        print("The entered character is a lowercase letter.")
else:
    print("The entered character is not an alphabet.")
