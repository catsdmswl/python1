h = int(input("키를 입력하세요. :"))
w = int(input("몸무게를 입력하세요. :"))
h_m=h/100
BMI = w / (h_m**2)
print('BMI:',BMI)
if BMI <=18.5:
    print("저체중입니다.")
elif BMI > 18.5 and BMI <= 25.0:
    print("적정체중입니다.")
else:
    print("과체중입니다.")