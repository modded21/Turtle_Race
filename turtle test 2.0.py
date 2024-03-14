# Turtle Game using the package 'turtle'.

# Import relevant modules
import turtle
import random
import time

# Setting up a nice screen for our game!
screen = turtle.Screen()
screen.bgcolor('lightblue') # Background a lightblue color

# We want four players in this game and the idea is that whoever
# gets to the other side wins!

# PLayer one - basic set up
player_one = turtle.Turtle()
# color of player one
player_one.color('blue')
# Make this player at turtle!
player_one.shape('turtle')

# Player two - basic set up
player_two = turtle.Turtle()
# color of player two
player_two.color('red')
player_two.shape('turtle')

# Player three -  basic set up
player_three = turtle.Turtle()
# color of player three
player_three.color('yellow')
player_three.shape('turtle')

# Player three -  basic set up
player_four = turtle.Turtle()
# color of player four
player_four.color('green')
player_four.shape('turtle')


# Let's position our players.
player_one.penup()
player_one.goto(-300, 200)
player_two.penup()
player_two.goto(-300, -200)
player_three.penup()
player_three.goto(-300, 100)
player_four.penup()
player_four.goto(-300, -50)

# Now let's draw a finish line.
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish!', font=24)

# Aloows player one to return to its starting position.
player_one.penup()
player_one.color('blue')
player_one.goto(-300, 200)
player_one.right(90)

# Ensuring all players put their pens down.
player_one.pendown()
player_two.pendown()
player_three.pendown()
player_four.pendown()

# Creating values for the die.
die = [1, 2, 3, 4, 5, 6]

# Creating the game!!
for i in range(30):
    if player_one.pos() > (300, 250):
        player_one.write("Player one wins the race!", font=24) 
    elif player_two.pos() > (300, -250):
        player_two.write("Player Two wins the race!", font=24)
    elif player_three.pos() > (300, 250):
        player_three.write("Player Three wins the race!", font=24)
    elif player_four.pos() > (300, -250):
        player_four.write("Player four wins the race!", font=24)

    else:
        die_roll = random.choice(die)
        player_one.forward(30*die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30*die_roll2)
        time.sleep(1)
        die_roll3 = random.choice(die)
        player_three.forward(30*die_roll3)
        time.sleep(1)
        die_roll4 = random.choice(die)
        player_four.forward(30*die_roll4)
        time.sleep(1)

# Get turtle to terminate when a player wins the race.
    if player_one.pos()  > (300, 250):
        quit()
    elif player_two.pos()  > (300, 250):
        quit()
    elif player_three.pos()  > (300, 250):
        quit()
    elif player_four.pos()> (300, 250):
        quit() 

   
    

# This keeps the turtle drawing on the screen!
turtle.done()
