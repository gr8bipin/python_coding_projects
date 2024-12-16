# The Python script creates a visual display of randomly generated stars on the screen using the turtle graphics module. 
# Importing Modules
import turtle as t # Imports the turtle module, which is used for drawing shapes.
from random import randint, random # Imported from the random module to generate random integers and floating-point numbers, respectively.

def draw_star(points, size, col, x, y): # The draw_star function, points: no. of points in the star, size: length of each other's side, col: color of the star, represented as an RGB tuple, x and y: coordinates where the star will be drawn
    
    # Function steps
        # Move to the starting position
    t.penup() # lifts the pen to move without drawing
    t.goto(x, y) # moves the turtle to the (x, y) position
    
    # Calculate the angle
    angle = 180 - (180 / points) # Determines the turning angle for the star. The formula ensures that the lines of the star connect correctly.
    t.color(col) # sets the open color
    t.begin_fill() # starts filling the shape with the specified color
    
    for i in range(points): # The for loop iterates through the number of points, drawing one segment of the star at a time:
        t.forward(size) # moves forward by the length of the star side
        t.right(angle) # turns the turtle to create the correct angle for the star
    t.end_fill() # fills the star with the current color

# setting the background
t.Screen().bgcolor('dark blue') # sets the background color of the canvas to dark blue, creating a "night sky" effect

# main loop
# The while True loop continuously generates and draws random stars:
# generate random star attributes

while True:
    ranPts = randint(2, 5) * 2 + 1 # randomly selects an odd number between 5 and 11 (inclusive) for the number of star points. Star must have an odd number of points to connect properly.
    ranSize = randint(10, 50) # randomly selects the size of the star between 10 and 50 pixels
    ranCol = (random(), random(), random()) # randomly generates an RGB color tuple where each value is a floating-point number between 0 and 1
    ranX = randint(-350, 300) # Randomly selects the position of the star within a range of coordinates.
    ranY = randint(-250, 250) # Randomly selects the position of the star within a range of coordinates.

    # Draw the star
    draw_star(ranPts, ranSize, ranCol, ranX, ranY) # calls the draw_star function with the randomly generated parameters

# Continuous Star Generation:
    # The while True loop runs indefinitely, continuously generating stars with random attributes and positions. Each star is unique in:
    # Number of points
    # Size
    # Color
    # Location

# How it works?
    # When you run the script:
    # A blank dark blue canvas appears, resembling a night sky.
    # Randomly generated stars are drawn one by one, each with different shapes, sizes, colors and positions.
    # This continues indefinitely until you manually stop the program (eg., by closing the window or pressing Ctrl + C in the terminal).

# Visual Output:
# You will see a dynamic "starry night" effect where stars of various colors and shapes populate the dark blue screen randomly, creating an aesthetically pleasing display.