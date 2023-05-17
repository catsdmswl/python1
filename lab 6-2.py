# 사용자로부터 입력받는다.
t = int(input("1.삼각형 2.평행사변형: "))
a = int(input("정수를 입력하세요 "))

if t==1: #t가 1이면
 # 별피라미드를 만든다.
 for i in range(a):
    for k in range(a,i,-1):
        print(' ',end='')

    for k in range((i+1)*2-1):
        print("*",end='')
    print()
else: #그렇지 않으면
    # 계단형태를 만든다.
    for i in range(a):
        for j in range(a, 0, -1):
            if (j > i):
                print(' ', end='')
            else:
                y = i
                print(y, end='')
        print()
    #역계단형태를 만든다.
    for num in range(a, 0, -1):
        for k in range(num):
            print(num, end='')
        print()