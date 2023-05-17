print("원금이 두배가 되는데 걸리는 시간입니다.") #문장을 출력한다.
from numpy import log as ln #자연로그 함수 불러온다.
for i in range(1,11,1):  # 1부터 10까지 반복
    year=ln(2)/ln(1+i/100) # 원금이 2배가 되는 데 걸리는 연도 계산한다.
    n=i
    print('이자율이', n,'%일 경우','%.0f년이 결립니다.'%(year)) #결과를 출력한다.




