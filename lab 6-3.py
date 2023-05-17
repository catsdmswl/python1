import random #랜덤 모듈 불러온다.
guess = 0;
tries = 0
answer = random.randint(0, 50) #0~50사이의 수 랜덤으로 추출한다.
while guess !=answer: #사용자가 입력한 값과 정답이 다르면
    guess = int(input('숫자를 맞추어보세요:')) #사용자로부터 값을 입력받는다.
    tries+=1 #시도횟수에 1을 더한다.
    if guess < answer: #사용자가 입력한 값이 정답보다 작으면
        print(guess,'은(는) 컴퓨터가 생각한 수보다 작습니다.')
    if guess > answer: #사용자가 입력한 값이 정답보다 크면
        print(guess, '은(는) 컴퓨터가 생각한 수보다 큽니다.')

print('맞추었습니다!!!')
print('총',tries,'회 시도했습니다.')
