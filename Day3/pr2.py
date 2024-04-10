def outer_function():
    print("This is outer_function.")

    def inner_function():
        print("This is inner_function.")

    print("Calling inner_function from outer_function:")
    inner_function()

# Invoke outer_function
outer_function()
