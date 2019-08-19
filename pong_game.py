# simple pong game

import turtle
import winsound

# creating a window for the game
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
    # center of screen is 0 -- +300 top, +300 bot, +400 left, +400 right
#stops window from updating...to speed up game
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a=turtle.Turtle()
# set speed of paddle 
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# don't have lines visible when moving object 
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b=turtle.Turtle()
# set speed of paddle 
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball 
ball=turtle.Turtle()
# set speed of ball 
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
# ball movement
ball.dx=.1
ball.dy=.1

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    
    
# Keyboard Binding
# listen for keyboard input
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



# Main game loop
while True:
    # updates the screen
    wn.update()
    
    # move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        # reverse direction when hitting border
        ball.dy *= -1
        winsound.PlaySound("Pong Game\sounds\bounce.wav", winsound.SND_FILENAME)

    if ball.ycor() < -290:
        ball.sety(-290)
        # reverse direction when hitting border
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)       
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)        
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1