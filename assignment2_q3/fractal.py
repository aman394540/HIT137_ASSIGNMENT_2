import turtle
import math


def _koch_inward_edge(t, length: float, depth: int) -> None:
    """
    Draws a single edge with inward Koch-like recursion.
    Each edge is divided into 3 segments, middle replaced with an inward triangle.
    """
    if depth == 0:
        t.forward(length)
        return

    segment = length / 3.0
    _koch_inward_edge(t, segment, depth - 1)
    t.right(60)  # inward dent start
    _koch_inward_edge(t, segment, depth - 1)
    t.left(120)
    _koch_inward_edge(t, segment, depth - 1)
    t.right(60)  # return to baseline
    _koch_inward_edge(t, segment, depth - 1)


def draw_polygon_pattern(n_sides: int, side_length: float, depth: int) -> None:
    """
    Draws a recursive polygon pattern:
    - n_sides: number of sides (>=3)
    - side_length: length of each side in pixels
    - depth: recursion depth (>=0)
    """
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.title(f"Inward Koch Polygon | sides={n_sides}, side={side_length}, depth={depth}")

    t = turtle.Turtle()
    t.speed(0)      # fastest drawing
    t.hideturtle()
    t.penup()

    # Position roughly so polygon is centered
    inradius = side_length / (2 * math.tan(math.pi / n_sides))
    t.goto(-side_length / 2, -inradius / 2)
    t.setheading(0)
    t.pendown()

    exterior_angle = 360.0 / n_sides

    for _ in range(n_sides):
        _koch_inward_edge(t, side_length, depth)
        t.left(exterior_angle)

    turtle.done()
