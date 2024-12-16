# importing libraries
import turtle # A module for creating graphics in Python.
from itertools import cycle # Import cycle function # A function that cycles through a list of items indefinitely. In this case, it cycles through colors.

# Setting up the colors
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple']) # A list of six colors is created, and cycle allows these colors to reapeat continuosly.

# Defining the draw_circle function
def draw_circle(size, angle, shift): 
    turtle.pencolor(next(colors)) # Picks the next color from the cycle.
    turtle.circle(size) # Draws a circle with the specified radius ('size').
    turtle.right(angle) # Rotates the turtle by 'angle' degrees to the right.
    turtle.forward(shift) # Moves the turtle forward by 'shift' units.
    draw_circle(size + 5, angle + 1, shift + 1) # Recursive call with updated parameters.

# Configuring the turtle environment. 
# These settings enhance the visual appeal of the spiral pattern.
turtle.bgcolor('black') # Sets the background color to black.
turtle.speed('fast') # Sets the drawing speed to fast.
turtle.pensize(8) # Sets the thickness of the pen to 4.

# Starting the drawing.
draw_circle(30, 0, 1) # Initial circle: Starts with a radius of 30 units, no rotation (angle = 0), and a forward shift of 1 unit.

# Purpose: Draws circles recursively while changing their size, rotation angle, and position.
# Parameters: 
    # size: Radius of the circle.
    # angle: Angle by which the turtle rotates before drawing the next circle.
    # shift: Distance the turtle moves forward before drawing next circle.
# Recursive call: The function calls itself with incremented values of size, angle, and shift, creating a dynamic pattern.

# How the spiral forms?
    # The first circle is drawn with a radius of 30.
    # The turtle rotates slightly (angle increases with each recursive call), moves forward (shift increases), and draws the next circle with a larger radius (size + 5).
    # This process repeats recursively, creating a spiral pattern with:
        # Gradually increasing circle sizes.
        # Slightly rotating angles between circles,
        # Shifting positions, so the circles form a spiraling effect.
    # The colors cycle, changing the pen color for each circle.