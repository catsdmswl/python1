n=int(input('임의의 정수를 입력하세요:')) #사용자로부터 정수 입력받는다.
a=0

for i in range(2,n+1):  # 2부터 n까지 반복
        if n % i**0.5 == 0: # 소수가 아니면
            a+=1 # a에 1를 더한다.
        else: # 소수이면
            a=0 #a=0

if a!=0: # a=0이 아니면
    print('임의의 정수',n,'는 소수가 아닙니다.') # 소수가 아님을 출력한다.
else: # 그렇지 않으면
    print('임의의 정수', n, '는 소수입니다.') # 소수임을 출력한다.
