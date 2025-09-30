def read_input(prompt, min, max):
    execute = True
    while execute:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                print(f"you entered: {value}")
                print("Good bye!")
                execute = False
            else:
                print(f"\nOopppS!: {value} is out of range (i.e {value}, is greater than the max number expected {max}.).\n")
                print(f"Error: Please enter a number between {min} and {max}.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

read_input("Enter a number between 1 and 20: ", 1, 20)
