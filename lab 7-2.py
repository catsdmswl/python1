def factorial(n):
    if n == 1:  # n이 1일 때
        return 1  # 1을 반환하고 함수를 종료한다.
    return n * factorial(n - 1)  # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱한다.

x=int(input('정수를 입력하세요:')) #사용자로부터 입력받는다.
print(factorial(x)) #결과를 출력한다.
