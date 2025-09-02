from utils import get_int, get_float
from fractal import draw_polygon_pattern


def main():
    print("=== Recursive Inward Polygon Pattern ===")
    n_sides = get_int("Enter number of sides (>=3): ", min_val=3)
    side_length = get_float("Enter side length in pixels (>0): ", min_val=1)
    depth = get_int("Enter recursion depth (>=0): ", min_val=0)

    draw_polygon_pattern(n_sides, side_length, depth)


if __name__ == "__main__":
    main()
