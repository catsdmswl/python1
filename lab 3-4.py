r=int(input("원기둥 밑면의 반지름:"))
h=int(input("원기둥의 높이:"))
pi=3.14
v=pi*h*r**2
s=(2*pi*r**2)+2*pi*r*h
print("원기둥의 부피는",v,"이고 겉넓이는",s,"입니다.")
