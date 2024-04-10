def toggle_string(input_string):
    return input_string.swapcase()

# Example usage:
string_input = input("Enter a string: ")  # Accept a string from the user
toggled_string = toggle_string(string_input)  # Call the function to toggle the string
print("Toggled string:", toggled_string)  # Print the toggled string
