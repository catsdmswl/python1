a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

D=b**2-4*a*c
e="방정식 %.2fx^2+%.2fx+%.2f"%(a,b,c)

if D<0:
    x6 =abs(D)
    x4= -b/ (2 * a)
    x5 = (x6 ** 0.5) / (2 * a)
    print(e,'는 서로 다른 두 허근 %.2f + %.2fi와 %.2f - %.2fi'%(x4,x5,x4,x5),'을 갖습니다.')
elif D==0:
    x1 = -b / 2*a
    print(e,"는 중근 %.2f"%(x1),'을 갖습니다.')
else:
    x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x3 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print(e,'는 서로 다른 두 실근 %.2f와 %.2f'%(x2,x3),'을 갖습니다.')
