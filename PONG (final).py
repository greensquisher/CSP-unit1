import turtle
import random
import time
accent = "white"
bg = "dodgerblue"
global run
run = 0
speed = 5
win = "PONG"
colorchoice = ["forestgreen", "limegreen", "burlywood", "antiquewhite", "darkgreen", "slategrey", "lightsteelblue", "cornflowerblue", "green", "lime", "royalblue", "ghostwhite", "black", "dimgray", "dimgrey", "gray", "grey", "darkgray", "darkgrey", "bisque", "darkorange", "tan", "navajowhite", "blanchedalmond", "papayawhip", "moccasin", "oldlace", "floralwhite", "darkgoldenrod", "goldenrod", "cornsilk", "seagreen", "mediumseagreen", "springgreen", "mintcream", "mediumspringgreen", "mediumaquamarine", "aquamarine", "turquoise", "lightseagreen", "mediumturquoise", "azure", "lavender", "midnightblue", "navy", "darkblue", "mediumblue", "blue", "slateblue", "darkslateblue", "mediumslateblue", "mediumpurple", "silver", "lightgray", "lightgrey", "orange", "gainsboro", "wheat", "whitesmoke", "white", "snow", "rosybrown", "lightcoral", "indianred", "gold", "lightcyan", "maroon", "brown", "firebrick", "lemonchiffon", "khaki", "palegoldenrod", "paleturquoise", "darkslategray", "darkslategrey", "darkred", "darkkhaki", "teal", "rebeccapurple", "blueviolet", "indigo", "darkorchid", "darkviolet", "mediumorchid", "red", "ivory", "darkcyan", "thistle", "mistyrose", "beige", "aqua", "plum", "salmon", "lightyellow", "cyan", "violet", "tomato", "lightgoldenrodyellow", "darkturquoise", "purple", "darksalmon", "olive", "cadetblue", "darkmagenta", "coral", "yellow", "powderblue", "fuchsia", "orangered", "olivedrab", "lightblue", "magenta", "lightsalmon", "yellowgreen", "deepskyblue", "orchid", "sienna", "darkolivegreen", "skyblue", "mediumvioletred", "seashell", "greenyellow", "lightskyblue", "deeppink", "chocolate", "chartreuse", "steelblue", "hotpink", "saddlebrown", "lawngreen", "aliceblue", "lavenderblush", "sandybrown", "honeydew", "dodgerblue", "peachpuff", "darkseagreen", "lightslategray", "peru", "palegreen", "lightslategrey", "linen", "lightgreen", "slategray", "palevioletred", "crimson", "pink", "lightpink"]

# Create a screen object
screen = turtle.Screen()
screen.setup(width=700, height=600)
screen.bgcolor(bg)
title=turtle.Turtle()
# Register a custom shape for the paddle
screen.register_shape("pong", ((-5, -45), (-5, 45), (5, 45), (5, -45)))

def start():
    global run
    global win
    if run ==1:
        win = "PONG"
        screen.clear()
        screen.bgcolor(bg)
        # Create the player 
        player = turtle.Turtle()
        player.shape("pong")
        player.color(accent)
        player.penup()
        player.speed(0)
        player.fd(300)
        player.right(90)
        player.forward(0)

        #create the cpu
        cpu = turtle.Turtle()
        cpu.shape("pong")
        cpu.color(accent)
        cpu.penup()
        cpu.speed(0)
        cpu.back(300)
        cpu.right(90)
        cpu.forward(0)

        #create the ball
        ball = turtle.Turtle()
        ball.shape("square")
        ball.color(accent)
        ball.turtlesize(.5)
        ball.penup()
        ball.hideturtle()
        ball.setheading(0)
        ball.speed(0)
        #Movement
        def move_up():
            if player.ycor() < 250:
                player.backward(20)
        def move_down():
            if player.ycor() > -230:
                player.forward(20)
        ball.goto(0,random.randint(-100,100))
        ball.showturtle()
        time.sleep(2)
        global speed
        while run == 1:
            screen.listen()
            ball.fd(speed)
            screen.onkey(move_up, "w")
            screen.onkey(move_down, "s")
            if abs(player.xcor()-ball.xcor()) < 10:
                if abs(player.ycor()-ball.ycor()) < 50:
                    if abs(player.ycor()-ball.ycor()) < 35:
                        ball.setheading(180)
                        ball.fd((speed*2)+1)
                    else:
                        if (player.ycor()-ball.ycor()) < -20:
                            ball.setheading(160)
                            ball.fd((speed*2)+1)
                        else:
                            ball.setheading(200)
                            ball.fd((speed*2)+1)
            elif abs(cpu.xcor()-ball.xcor()) < 10:
                if abs(cpu.ycor()-ball.ycor()) < 50:
                    if abs(cpu.ycor()-ball.ycor()) < 35:                
                        ball.setheading(0)
                        ball.fd((speed*2)+1)
                    else:
                        if (cpu.ycor()-ball.ycor()) < -20:
                            ball.setheading(20)
                            ball.fd((speed*2)+1)
                        else:
                            ball.setheading(-20)
                            ball.fd((speed*2)+1)
            if ball.xcor() > 310:
                win = "Loose!"
                run = 0
                screen.clear()
                titlescreen()
            if ball.xcor() < -310:
                win = "Win!"
                run = 0
                screen.clear()
                titlescreen()
            if ball.ycor() > 280:
                ball.right(45)
            if ball.ycor() < -280:
                ball.right(45)
            if (cpu.ycor()-ball.ycor()) > 50:
                if cpu.ycor() > (-150-(speed*speed)):
                    cpu.forward(20)
            if (cpu.ycor()-ball.ycor()) < -50:
                if cpu.ycor() < (180+(speed*speed)):
                    cpu.backward(20)
        turtle.clearscreen()
        screen.bgcolor(str(bg))
    run = 1

def colors():
    global bg
    global accent
    global speed
    global colorchoice
    global win
    win = "PONG"
    screen.clear()
    screen.bgcolor(bg)
    title.goto(-200, 200)
    accent = turtle.textinput("Accent color", "Please enter a color:")
    while accent not in colorchoice:
        accent = turtle.textinput("Accent color", "Please enter a color:")
    bg = turtle.textinput("Background color", "Please enter a color:")
    while bg not in colorchoice:
        bg = turtle.textinput("Background color", "Please enter a color:")
    speed = int(turtle.textinput("Difficulty", "Please enter a number 1-10"))
    speed = speed*2
    screen.bgcolor(bg)
    global run
    run = 1
    start()

def titlescreen():
    while True:
        global win
        global run
        run = 0
        title.hideturtle()
        title.penup()
        title.goto(0,0)
        title.color(accent)
        screen.bgcolor(str(bg))
        title.write(win, align="center", font=("Futura", 200, "normal")) 
        title.goto(0, -50)
        title.write("Press 'S' to change settings", align="center", font=("Futura", 30, "normal"))
        title.goto(0,-80)
        title.write("Hold 'W' to start a game", align="center", font=("Futura", 30, "normal"))
        title.goto(0,-110)
        title.write("Use 'W' and 'S' keys to move", align="center", font=("Futura", 30, "normal"))

        screen.listen()
        screen.onkey(colors, "s")
        screen.onkey(start, "w")
titlescreen()
wn = turtle.Screen
turtle.mainloop()