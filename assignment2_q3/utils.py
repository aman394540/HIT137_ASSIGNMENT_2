def get_int(prompt: str, min_val: int = None) -> int:
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Enter an integer >= {min_val}.")
                continue
            return val
        except ValueError:
            print("Invalid integer. Try again.")


def get_float(prompt: str, min_val: float = None) -> float:
    while True:
        try:
            val = float(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Enter a number >= {min_val}.")
                continue
            return val
        except ValueError:
            print("Invalid number. Try again.")
