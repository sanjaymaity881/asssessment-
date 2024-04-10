def process_input(input_string, min_length=3, max_length=5):
    if min_length <= len(input_string) <= max_length:
        print("Input accepted:", input_string)
    else:
        print("Input must be between", min_length, "and", max_length, "characters.")

# Example usage:
input_str = input("Enter a string (minimum 3 characters, maximum 5 characters): ")
process_input(input_str)
