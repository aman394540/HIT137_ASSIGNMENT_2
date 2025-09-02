# Function to safely get an integer input from the user
def get_int(prompt: str, min_val: int = None) -> int:
    while True:  # Keep asking until valid input is given
        try:
            # Try to convert the user’s input into an integer
            val = int(input(prompt))
            
            # If a minimum value is required, check it
            if min_val is not None and val < min_val:
                # This message is shown to the user, not a comment
                print(f"Enter an integer >= {min_val}.")
                continue  # Ask again if the condition fails
            
            return val  # Return the valid integer
        
        except ValueError:
            # If input cannot be converted to int, show error to the user
            print("Invalid integer. Try again.")


# Function to safely get a floating-point input from the user
def get_float(prompt: str, min_val: float = None) -> float:
    while True:  # Keep asking until valid input is given
        try:
            # Try to convert the user’s input into a float
            val = float(input(prompt))
            
            # If a minimum value is required, check it
            if min_val is not None and val < min_val:
                # This message is shown to the user, not a comment
                print(f"Enter a number >= {min_val}.")
                continue  # Ask again if the condition fails
            
            return val  # Return the valid float value
        
        except ValueError:
            # If input cannot be converted to float, show error to the user
            print("Invalid number. Try again.")
