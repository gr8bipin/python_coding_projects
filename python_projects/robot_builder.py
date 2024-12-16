# import turtle as t
import turtle as t  # the turtle module is imported and aliased as t for convenience

# Drawing a Rectangle Function
def rectangle(horizontal, vertical, color): # defines a function named rectangle to draw a rectangle with specified width (horizontal), height (vertical) and color
    t.pendown() # puts the pen down to start drawing
    t.pensize(1) # sets the thickness of the pen to 1 unit
    t.color(color) # sets the pen and fill color
    t.begin_fill() # starts filling the shape with the selected color

    for counter in range(1, 3): # loops twice to draw the four sides of the rectangle
        t.forward(horizontal) # Draws the horizontal side of the rectangle, moves forward by horizontal units (width)
        t.right(90) # Turns the turtle 90 degree to the right. 
        t.forward(vertical) # moves forward by vertical units (height)
        t.right(90) # Turns 90 degrees to complete one rectangle side
    
    t.end_fill() # fills the drawn rectangle with specified color
    t.penup() # lifts the pen to stop drawing when the turtle moves

t.penup() # ensures the pen is  lifted before positioning the turtle
t.speed('slow') # the turtle's drawing speed is set to'slow' 
t.bgcolor('Dodger blue') # the background color is set to 'Dodger blue'

# feet
t.goto(-100, -150) # moves the turtle to co-ordinates (-100, -150)
rectangle(50, 20, 'blue') # draws a blue rectangle (50 wide, 20 tall) for the left foot
t.goto(-30, -150) # moves the turtle to co-ordinates (-30, -150)
rectangle(50, 20, 'blue') # draws a blue rectangle (50 wide, 20 tall) for the right foot

# legs
t.goto(-25, -50) # moves to (-25, -50)
rectangle(15, 100, 'grey') # draws a grey rectangle (15 wide, 100 tall) for the right leg
t.goto(-55, -50) # moves to (-55, -50)
rectangle(-15, 100, 'grey') # attempts to draw a rectangle with a negative width (-15), which is invalid and will cause an error

# body
t.goto(-90, 100) # moves to (-90, 100) 
rectangle(100, 150, 'red') # draws a red rectangle (100 wide, 150 tall) for the body

# arms
t.goto(-150, 70) # moves to (-150, 70)
rectangle(60, 15, 'grey') # draws a grey rectangle (60 wide, 15 tall) for the left arm

t.goto(-150, 110) # moves to (-150, 110)
rectangle(15, 40, 'grey')  # draws a grey rectangle (15 wide, 40 tall) for the left arm

t.goto(10, 70) # moves to (10, 70)
rectangle(60, 15, 'grey') # draws a grey rectangle (60 wide, 15 tall) for the right arm

t.goto(55, 110) # moves to (55, 110)
rectangle(15, 40, 'grey') # draws a grey rectangle (15 wide, 40 tall) for the upper part of the right arm

# neck
t.goto(-50, 120) # moves to (-50, 120)
rectangle(15, 20, 'grey') # draws a grey rectangle (15 wide, 20 tall) for the neck

# Head
t.goto(-85, 170) # moves to (-85, 170)
rectangle(80, 50, 'red') # draws a red rectangle (80 wide, 50 tall) for the head

# Eyes
t.goto(-60, 160) # moves to (-60, 160)
rectangle(30, 10, 'white') # draws a white rectangle (30 wide, 10 tall) for the left eye

t.goto(-55, 155) # moves to (-50, 155)
rectangle(5, 5, 'black') # draws a small black rectangle (5 wide, 5 tall) for the right pupil

# Mouth
t.goto(-65, 135) # moves to (-65, 135)
rectangle(40, 5, 'black') # draws a black rectangle (40 wide, 5 tall) for the mouth

# final steps
t.hideturtle() # hides the turtle pointer for a cleaner final drawing

# Key points
    # coordinate system: the turtle moves to specific (x, y) positions using t.goto(x,y)
    # modular code: the rectangle function is reusable, making the code concise
    # visual elements: each rectangle is drawn with specific dimensions and colors to assemble the robot

