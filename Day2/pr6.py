def toggle_character(char):
    return char.swapcase()

# Example usage:
character = input("Enter a character: ")  # Accept a character from the user
toggled_character = toggle_character(character)  # Call the function to toggle the character
print("Toggled character:", toggled_character)  # Print the toggled character
