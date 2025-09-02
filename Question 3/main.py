# Import helper functions from utils.py
from utils import get_int, get_float

# Import the recursive fractal drawing function from fractal.py
from fractal import draw_polygon_pattern


def main():
    # Title of the program
    print("=== Recursive Inward Polygon Pattern ===")
    
    # Ask user for number of sides of the polygon (minimum 3 for a valid polygon)
    n_sides = get_int("Enter number of sides (>=3): ", min_val=3)
    
    # Ask user for the length of each side (must be greater than 0)
    side_length = get_float("Enter side length in pixels (>0): ", min_val=1)
    
    # Ask user for the recursion depth (0 = no recursion, higher values = more detail)
    depth = get_int("Enter recursion depth (>=0): ", min_val=0)

    # Call the function to draw the recursive polygon pattern
    draw_polygon_pattern(n_sides, side_length, depth)


# Standard Python entry point check
# Ensures main() runs only if this file is executed directly
if __name__ == "__main__":
    main()
