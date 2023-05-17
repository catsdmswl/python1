x1=int(input("첫 번째 점의 x좌표:"))
y1=int(input("첫 번째 점의 y좌표:"))
x2=int(input("두 번째 점의 x좌표:"))
y2=int(input("두 번째 점의 y좌표:"))
import math
d=(math.sqrt((x1-x2)**2+(y1-y2)**2))
print("두 점 (",x1,y1,") 사이의 거리는",d,"입니다.")