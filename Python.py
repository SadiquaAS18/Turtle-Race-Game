*SOFTWARE CODE*

# Python Turtle Race

import turtle
import random
screen = turtle.Screen()
screen.title("Turtle Race")
turtles = []
colors = ["red", "blue", "green", "orange", "purple", "brown"]
for i in range(6):
 new_turtle = turtle.Turtle()
 new_turtle.shape("turtle")
 new_turtle.color(colors[i])
 new_turtle.penup()
 new_turtle.goto(-200, 100 - i * 40)
 turtles.append(new_turtle)
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(200, 200)
finish_line.pendown()
finish_line.goto(200, -200)
def race():
 while True:
 for turtle in turtles:
 turtle.forward(random.randint(1, 5))
 if turtle.xcor() >= 200:
 winner_color = turtle.color()[0]
 if winner_color == "red":
 winner = "Red Turtle"
 elif winner_color == "blue":
 winner = "Blue Turtle"
 elif winner_color == "green":
 winner = "Green Turtle"
 elif winner_color == "orange":
 winner = "Orange Turtle"
 elif winner_color == "purple":
 winner = "Purple Turtle"
 else:
 winner = "Brown Turtle"
 turtle.goto(-200, 100 - turtles.index(turtle) * 40)
 return winner
winner = race()
screen.title(f"{winner} Wins!")
turtle.done()
