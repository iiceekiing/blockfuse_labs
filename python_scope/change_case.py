
import time

def case_changer(s: str) -> str:

    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    elif s == "":
        raise ValueError("hello Ekuke! your input cannot be empty\n Please enter a valid string")

    
    elif s.isspace():
        raise ValueError("Oopps!: Input string cannot be just whitespace\ncannot convert empty string to upper/lower case")
    
    elif any(char.isdigit() for char in s):
        raise ValueError("Input string cannot contain numbers")
    
    elif any(not char.isalnum() and not char.isspace() for char in s):
        raise ValueError("Input string cannot contain special characters")

    elif s != s.strip():
        raise ValueError("Input string cannot have leading or trailing whitespace")
    
    elif s.isupper():
        print(f"Input {s} is already in uppercase")
        print("converting to lowercase...")
        time.sleep(1)  
        return s.lower()
    
    elif s.islower():
        print(f"Input {s} is already in lowercase")
        print("converting to uppercase...")
        time.sleep(1)
        return s.upper()


if __name__ == "__main__":
    print(case_changer("this file was run directly, so the interactive session will be activated next."))
    print("To exit the interactive session, type exit and press Enter.")
    time.sleep(2)
    interact = input("Enter Anything: ")

    if interact.lower() == "exit":
        print("Exiting the interactive session. Goodbye!")
        time.sleep(1)
    else:
        print(f"you type '{interact}'. it has been transformed into {case_changer(interact)}.")