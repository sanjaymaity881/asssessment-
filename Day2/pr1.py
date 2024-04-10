# Define function to add
def add():
    print("Calling add() function...")

# Define function to modify
def modify():
    print("Calling modify() function...")

# Define function to delete
def delete():
    print("Calling delete() function...")

# Accept input from the user
try:
    user_input = int(input("Enter a number (1 for add, 2 for modify, 3 for delete): "))
    
    # Match user input to call appropriate function
    match user_input:
        case 1:
            add()
        case 2:
            modify()
        case 3:
            delete()
        case _:
            print("Invalid input. Please enter 1, 2, or 3.")
except ValueError:
    print("Invalid input. Please enter a number.")
