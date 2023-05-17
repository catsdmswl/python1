import turtle
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)
t.penup()
t.goto(100, -100)
t.pendown()
t.circle(100)
t.penup()
t.goto(50, 0)
t.pendown()
t.circle(100)
t.penup()

x=int(input('x좌표를 입력하세요:'))
y=int(input('y좌표를 입력하세요:'))
t.goto(x, y)
t.pendown()
t.dot(20)

a=(0-x)**2+(0-y)**2
b=(100-x)**2+(0-y)**2
c=(50-x)**2+(100-y)**2
if a<=100**2 and b<=100**2 and c<=100**2:
    print((x,y),'를 포함하는 원은 3개 있습니다.')
elif a > 100 **2 and b > 100 **2 and c > 100 **2:
    print((x, y), '를 포함하는 원은 0개 있습니다.')
elif a <= 100 **2 and b > 100 **2 and c > 100 **2:
    print((x, y), '를 포함하는 원은 1개 있습니다.')
elif b <= 100 **2 and a > 100 **2 and c > 100 **2:
    print((x, y), '를 포함하는 원은 1개 있습니다.')
elif c <= 100 **2 and b > 100 **2 and a > 100 **2:
    print((x, y), '를 포함하는 원은 1개 있습니다.')
else:
    print((x, y), '를 포함하는 원은 2개 있습니다.')

turtle.done()