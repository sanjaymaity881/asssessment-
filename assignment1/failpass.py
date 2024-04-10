# Function to determine result based on marks
def determine_result(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks < 40:
        return "Fail"
    elif marks < 50:
        return "Pass"
    elif marks < 60:
        return "Second Class"
    elif marks < 70:
        return "First Class"
    else:
        return "Distinction"

# Accept marks from the user
try:
    marks = float(input("Enter marks: "))
    result = determine_result(marks)
    print("Result:", result)
except ValueError:
    print("Please enter a valid numeric value for marks.")
