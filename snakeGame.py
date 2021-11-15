import turtle
import time
import random

delay=0.1

# ---------- creating the window ----------
win = turtle.Screen()
win.title("my snake game")
win.bgcolor("blue")
win.setup(width=600, height=600)
win.tracer(0)

# ---------- creating the snake's head ----------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup() #makes sure the the path taken by the snake isnt drawn
head.goto(0, 100)
head.direction = "stop"

#this updates the window continuously (check line 160)
# while True:
#     win.update()

# ---------- Functions to move the snake ---------
def move():
    if head.direction == "up":
        y = head.ycor() # y coordinate of the turtle
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor() # y coordinate of the turtle
        head.sety(y - 20)
 
    if head.direction == "right":
        x = head.xcor() # y coordinate of the turtle
        head.setx(x + 20)
 
    if head.direction == "left":
        x = head.xcor() # y coordinate of the turtle
        head.setx(x - 20)

# functions that tells the computer what directions are
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"

# keyboard bindings
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

# ---------- snake food ---------
# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# move the food to a random position on screen
if head.distance(food) < 15:
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

segments = []
# ---------- building the snake's body ---------
# add a segment
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("grey")
new_segment.penup()
segments.append(new_segment)

# move the end segment in reverse order
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

# Move segment 0 to where the head is
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

# Check for border collision
if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
 
    # clear segment list
    segments.clear()

# Check for head collision
for segment in segments:
    if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segment list
        segments.clear()

#adding scores
# score
score = 0
high_score = 0
# create pen to write score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "bold"))


# Increase the score
score = score+10

if score > high_score:
    high_score = score

    # reset score
    score = 0

    # update score
    pen.clear()
    pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "bold"))

#this updates the window continuously
while True:
    win.update()
    move()
    time.sleep(delay)
