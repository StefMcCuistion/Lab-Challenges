import turtle


screen = turtle.Screen()  # Opens window
screen.title("Get to know Turtle!")  # Renames window. Name appears in bar
# on top, in task manager, when hovering over the program in the taskbar, etc.
screen.setup(width=800, height=600)  # Sets window width and height in pixels
pen = turtle.Turtle()  # Initializes Turtle obj, no immediate effect

pen.width(10)  # Sets pen width, no immediate effect
pen.down()  # sets the "pen" down on the paper so that movement commands
# will leave a visible mark
pen.forward(distance=50)  # Draws a line from start point (center of screen?)
# to a point 50 pixels away. I don't know the pen's starting angle, probably
# up
pen.left(angle=90)  # Changes "forward" to be 90 degrees to the left
pen.backward(100)  # Moves 100 pixels in opposite direction of new forward
pen.right(90)  # change angle by 90 degrees to the right
pen.backward(100)  # Moves 100 pixels in opposite dir of forward
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.up()  # Stop drawing

pen.width(1)  # Line is 1/10 as thick as before
pen.goto(x=-100, y=50)  # New coordinates before pen goes down again
pen.color(1.0, 0.0, 0.0)  # Red color
pen.down()  # start drawing again
pen.fillcolor(0, 1, 0)  # Green fill color
pen.begin_fill()
pen.circle(radius=90)  # Draw red circle outline, 1 px thick, with green fill
# and 90 pixel radius
pen.end_fill()
pen.fillcolor(1, 1, 1)
pen.begin_fill()
pen.circle(30)  # Red circle outline 1 px thick with white fill, 30 px radius
pen.end_fill()
pen.fillcolor(0, 1, 0)
pen.begin_fill()
pen.circle(10)  # Red circle outline 1 px thick with green fill, 10 px radius
pen.end_fill()
pen.up()
# Will the circles be concentric, or will their circumferences share a point
# somewhere, such as at the top, from which they're all drawn?
# I'm guessing concentric, meaning they're drawin from the center

screen.exitonclick()


# Predict what the code does using code comments.

# Run the code to confirm your predictions.

# Investigate:

# Why does the code use the .up() and .down() methods?

# Where do you think .goto(0, 0) will bring the cursor on the screen?

# How does pen.goto(x=-100, y=50) and pen.goto(-100, -150) both work?
# When might one explicitly use the argument keywords x and y?
