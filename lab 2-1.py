
x=int(input("직사각형의 가로:"))
y=int(input("직사각형의 세로:"))
print(x,"는 직사각형의 가로이고",y,"는 직사각형의 세로 입니다.")

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.forward(x)
t.right(90)
t.forward(y)
t.right(90)
t.forward(x)
t.right(90)
t.forward(y)
turtle.done()
