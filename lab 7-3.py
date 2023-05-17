#함수를 계산한다.
def y(x):
    result = x**2 + 1
    return result
n=int(input('x좌표를 입력하세요:')) #사용자로부터 x값을 입력 받는다.
print('함수값:',y(n)) #결과를 출력한다.

#터틀 모듈 사용한다.
import turtle
t = turtle.Turtle()
#가로세로축 그린다.
t. pendown()
t. shape('turtle')
t.forward(250)
t. penup()
t. goto(0,250)
t.right(90)
t. pendown()
t.forward(250)
t.right(90)
# 함수 그래프 그린다.
for i in range(151):
    x=i
    y=(x**2 + 1)*0.01 #함수가 화면 밖으로 나가는 것을 방지하기 위해 0.01배 축소한다.
    t.goto(x,y)
turtle.done()
