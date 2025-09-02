import turtle
import math


# Helper function to draw a single edge using Koch-like inward recursion
def _koch_inward_edge(t, length: float, depth: int) -> None:
    """
    Draws a single edge with inward Koch-like recursion.
    Each edge is divided into 3 segments, middle replaced with an inward triangle.
    """
    if depth == 0:  # Base case: just draw a straight line
        t.forward(length)
        return

    # Divide edge into 3 equal segments
    segment = length / 3.0

    # Recursive drawing of first segment
    _koch_inward_edge(t, segment, depth - 1)

    # Create inward dent by turning right
    t.right(60)
    _koch_inward_edge(t, segment, depth - 1)

    # Draw middle triangle by turning left
    t.left(120)
    _koch_inward_edge(t, segment, depth - 1)

    # Return to original direction
    t.right(60)
    _koch_inward_edge(t, segment, depth - 1)


# Main function to draw the full recursive polygon pattern
def draw_polygon_pattern(n_sides: int, side_length: float, depth: int) -> None:
    """
    Draws a recursive polygon pattern:
    - n_sides: number of sides (>=3)
    - side_length: length of each side in pixels
    - depth: recursion depth (>=0)
    """
    # Setup drawing window
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.title(f"Inward Koch Polygon | sides={n_sides}, side={side_length}, depth={depth}")

    # Create turtle object
    t = turtle.Turtle()
    t.speed(0)      # fastest drawing speed
    t.hideturtle()  # hide turtle cursor
    t.penup()

    # Position turtle so polygon is roughly centered
    inradius = side_length / (2 * math.tan(math.pi / n_sides))
    t.goto(-side_length / 2, -inradius / 2)
    t.setheading(0)
    t.pendown()

    # Calculate exterior angle for polygon
    exterior_angle = 360.0 / n_sides

    # Draw all polygon sides with recursive edges
    for _ in range(n_sides):
        _koch_inward_edge(t, side_length, depth)
        t.left(exterior_angle)

    
    turtle.done()
