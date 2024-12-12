# import modules
import random # random for generating random positions for leaves
import turtle as t # turtle for creating a graphical interface with moving objects

t.bgcolor('yellow') # the game has a yellow background

# create caterpillar turtle
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# create caterpillar2 turtle
caterpillar2 = t.Turtle()
caterpillar2.color('blue')
caterpillar2.shape('square')
caterpillar2.penup()
caterpillar2.speed(0)
caterpillar2.hideturtle()

# create a leaf turtle
leaf = t.Turtle()

# co-ordinates for leaf shape
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))

# this line tells the turtle about the leaf shape
# it is a custom shape registered as leaf
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

# Add some text 
game_started = False # You'll need to know later if the game has started

text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align = 'center', font = ('Arial', 16, 'bold')) # this line draws some text on the screen
text_turtle.hideturtle() # this hides the turtle but not the text

score_turtle = t.Turtle() # add a turtle to write the score
score_turtle.hideturtle() 
score_turtle.speed(0) # the turtle needs to stay where it is, so that it can update the score

# Main Loop
# functions
# to get a basic version of the program running sooner, you can use placeholders for functions that you'll finish coding later
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos() # This function returns two values (a "tuple")

    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside # if any of the four conditions above is True, then outside is True

def outside_window(caterpillar):
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar2.pos() # This function returns two values (a "tuple")

    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside # if any of the four conditions above is True, then outside is True

def game_over():
    caterpillar.color('yellow')
    caterpillar2.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align = 'center', font = ('Arial', 30, 'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50 # 50 pixels from the right
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align= 'right', font=('Arial', 40, 'bold'))

def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200)) # chooses random coordinates to move the leaf
    leaf.sety(random.randint(-200, 200))
    leaf.st() # st is short for showturtle

# Game starter
def start_game():
    global game_started

# if the game has already started, the return command makes the function quit so it doesn't run a second time
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear() # clear the text from screen

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    caterpillar2.shapesize(1, caterpillar_length, 1)
    caterpillar2.setheading(180)
    caterpillar2.showturtle()
    display_score(score)
    place_leaf() # this line places the first leaf on the screen

    # Get moving
    while True:
        
        caterpillar.forward(caterpillar_speed)
        caterpillar2.forward(caterpillar_speed)

        if caterpillar.distance(leaf) < 20 or leaf.distance(caterpillar2) < 20: # the caterpillar eats the leaf when it's less than 20 pixels away
            place_leaf() # the current leaf has been eaten, so add a new leaf
            caterpillar_length = caterpillar_length + 1 # this will make the caterpillar grow longer
            caterpillar.shapesize(1, caterpillar_length, 1) # this will make the caterpillar grow longer
            caterpillar2.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)

        if outside_window(caterpillar) or outside_window(caterpillar2):
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180: # check if the caterpillar is heading left or right
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270) # A heading of 270 sends the caterpillar down the screen

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

# Bind and listen
t.onkey(start_game, 'space') # when you press the space bar, the game begins

t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')

def caterpillar2_move_up():
    if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
        caterpillar2.setheading(90)

def caterpillar2_move_down():
    if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
        caterpillar2.setheading(270)

def caterpillar2_move_left():
    if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
        caterpillar2.setheading(180)

def caterpillar2_move_right():
    if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
        caterpillar2.setheading(0)

t.onkey(caterpillar2_move_up, 'w')
t.onkey(caterpillar2_move_right, 'd')
t.onkey(caterpillar2_move_down, 's')
t.onkey(caterpillar2_move_left, 'a')

t.listen() # the listen() function allows the program to receive signals from the keyboard # listen() enables the program to detect and respond to keyboard input
t.mainloop() # main loop keeps the game running until explicitly closed
  
# Test your code
# start_game()

