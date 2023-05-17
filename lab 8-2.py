phone_book = {} #딕셔너리 생성한다.
while True: #참일 경우 반복한다.
    name = input('친구의 이름을 입력하세요:') #사용자로부터 이름을 입력받는다.
    if name == "": #줄바꿈키(엔터키)를 누른다면
        print('전화번호 검색 모드로 전환됩니다.') #전화번호 검색 모드 메시지 출력한다.
        x = input('친구의 이름을 입력하세요:') #찾으려는 이름을 입력받는다.
        print(x, '의 전화번호:', phone_book[x]) #key에 따른 value를 출력한다.
    elif name == '끝': #끝을 입력받으면
        print('프로그램을 종료합니다.') #프로그램을 종료한다.
        break
    else: #그렇지 않으면
        number = input('친구의 전화번호를 입력하세요:') #사용자로부터 전화번호를 입력받는다
        phone_book[name] = number #딕셔너리에 저장한다.
        print(phone_book) #딕셔너리를 출력한다.
