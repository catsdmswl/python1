import matplotlib.pyplot as plt #Matplotlib 라이브러리 사용한다.

#X의 범위는 -10에서 +10까지를 200등분한다.
xValues = []
for i in range(-100,100):
    xValues.append(i/10.0)

#2차 함수의 계수를 입력받는다.
a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))

#2차 함수값을 계산하여서 yValues에 저장한다.
yValues = []
for i in xValues:
  yValues.append(a*i**2 + b*i +c)

plt.plot(xValues, yValues) #x값, y값 설정한다.
plt.show() #그래프를 보여준다.
