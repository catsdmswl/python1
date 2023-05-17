import math
#원의 면적과 둘레 계산
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        self.round = 2 * math.pi * self.radius

    def get_area(self):
        self.area = math.pi * (self.radius ** 2)
#5개의 instance들을 만들어 list에 저장
circle_list = []
count = 0
c = 0
for _ in range(5):
    a = int(input('반지름을 입력하세요:'))
    circle_list.append(a)
    count += 1
print('생성되는 Object의 수는 %.f개 입니다.'%count)
#객체를 생성하여 method 실행
for radius in circle_list:
    Circles = Circle(radius)
    Circles.get_circumference()
    Circles.get_area()
    c +=1
    print("%.f번 원 - "%c,"반지름:",radius, "원의 면적:%.3f"%Circles.area, "원의 둘레:%.3f"%Circles.round)


