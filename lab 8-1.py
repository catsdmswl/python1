import random #랜덤 모듈 사용한다.
#아래의 배열 사용한다.
capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbol=['!','@','#','$','%']
number='0123456789'
password=''
for i in range(12): #12번 반복한다
   # 각 배열에서 랜덤으로 하나 추출한다.
   a = random.choice(capital)
   b = random.choice(small)
   c = random.choice(symbol)
   d = random.choice(number)
   result=[a,b,c,d] #랜덤으로 추출한 배열을 리스트로 만든다.
   x = random.choice(result) #랜덤으로 추출한 배열에서 하나를 랜덤으로 추출한다.
   password +=x #추출한 값을 반복할 때마다 더한다.

print('비밀번호:',password) #비밀번호를 출력한다.