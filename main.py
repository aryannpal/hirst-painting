import random
import turtle
from turtle import Turtle,Screen
# import colorgram
# colors=colorgram.extract('image.jpg',30)
# my_list=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     my_tuple=(r,g,b)
#     my_list.append(my_tuple)
# print(my_list)
turtle.colormode(255)

color_list=[(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
            (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
            (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
            (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
            (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
            (168, 99, 102)]


tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
dots=100

for num_of_dots in range(1,dots+1):
    tim.setheading(0)
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if num_of_dots % 10==0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
tim.hideturtle()
screen=Screen()

screen.exitonclick()