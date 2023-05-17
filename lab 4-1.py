
number_list = [ ]
number = int(input("리스트의 첫 번째 요소: "))
number_list.append(number)
number = int(input("리스트의 두 번째 요소: "))
number_list.append(number)
number = int(input("리스트의 세 번째 요소: "))
number_list.append(number)
number = int(input("리스트의 네 번째 요소: "))
number_list.append(number)
number = int(input("리스트의 다섯 번째 요소: "))
number_list.append(number)
print('입력받은 리스트:',number_list)

average = sum(number_list) / len(number_list)
x1=(number_list[0] - average)**2
x2 = (number_list[1] - average) ** 2
x3 = (number_list[2] - average) ** 2
x4 = (number_list[3] - average) ** 2
x5 = (number_list[4] - average) ** 2
vsum=x1+x2+x3+x4+x5
variance = vsum / len(number_list)
print('1.평균=',average,'분산=',variance)
print("2.역순:",number_list[::-1])
y1=min(number_list)
y2=number_list.index(y1)
number_list.remove(y1)
number_list.insert(y2,0)
print('3.최소값 변환 :',number_list)

