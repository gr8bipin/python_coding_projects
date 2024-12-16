# This python code draws an alternating pattern of circles and squares using the turtle graphics module. The pattern grows and shifts dynamically as the function recursively calls itself.

# Code Explanation:

# Importing libraries
import turtle # Used for creating 2D graphics and shapes.
from itertools import cycle # Cycles through a list of items indefinitely. In this case, it cycles through a list of colors.

# Setting up colors
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple']) # A list of six colors is created. cycle ensures the colors repeat endlessly as the pattern grows.

# Defining the recursive function
def draw_shape(size, angle, shift, shape): # Add a new parameter, shape.
    
    turtle.pencolor(next(colors)) # change the pen color to the next in the cycle
    
    next_shape = '' # Variable to store the shape for the next recursive call
    
    # Drawing Shapes
    
    # Case 1: Drawing a Circle
    if shape == 'circle':
        turtle.circle(size) # Draw a circle with the given radius.
        next_shape = 'square' # Set the next shape to be a square.
    
    # Case 2: Drawing a Square
    elif shape == 'square':
        for i in range(4): # The loop runs 4 times, once for each side of the square.
            turtle.forward(size * 2) # Draw each side of the square (length is 'size * 2')
            turtle.left(90) # Turn left by 90 degrees to form the square
        next_shape = 'circle' # Set the next shape to be a circle.
    
    # Adjusting Position and Recursion
    turtle.right(angle) # Rotate the turtle slightly to create a spiraling effect.
    turtle.forward(shift) # Move the turtle forward for the next shape.
    
    draw_shape(size + 5, angle + 1, shift + 1, next_shape) # next_shape makes the turtle alternate between circles and squares. # Recursive call with updated parameters

# Configuring Turtle Graphics
# These settings improve the visual appeal of the drawing.
turtle.bgcolor('black') # Sets the background color to black.
turtle.speed('fast') # Sets the turtle's speed to 'fast'.
turtle.pensize(4) # Sets the thickness of the pen to 4.

# Starting the Drawing
draw_shape(30, 0, 1, 'circle') # The first shape is a circle. 
# The drawing starts with:
    # A circle of size 30
    # An initial angle of 0 (no rotation)
    # A forward shift of 1 unit
    # The first shape is a "circle".

# Final Output: The program generates an alternating, colorful spiral of circles and squares against a black background.

# Parameters:
    # size: Determines the size of the current shape.
    # angle: Rotation angle applied after drawing each shape.
    # shift: Distance the turtle moves forward after drawing a shape.
    # shape: Specifies whether to draw a circle or a square.

# Angle: After each shape, the turtle rotates by the specified angle. This creates a spiraling effect.
# Shift: The turtle moves forward, creating space between shapes.
# Recursive call: The function is called again with updated parameters:
    # size + 5: Increases the size of the next shape.
    # angle + 1: Gradually increases the rotation angle.
    # shift + 1: Gradually increases the forward shift.
    # next_shape: Alternates between "circle" and "square"

