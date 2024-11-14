import turtle

def move_forward():
     north = 90 - turtle.heading()
     turtle.left(north)
     turtle.forward(100)
def move_backward():
     south = 270 - turtle.heading()
     turtle.left(south)
     turtle.forward(100)
def move_right():
     east = 0 - turtle.heading()
     turtle.left(east)
     turtle.forward(100)
def move_left():
    west = 180 - turtle.heading()
    turtle.left(west)
    turtle.forward(100)


turtle.onkey(move_forward, "Up")
turtle.onkey(move_backward, "Down")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


turtle.listen()
turtle.done()