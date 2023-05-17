import math

a = float(input("적분 구간을 입력하세요 a : "))
b = float(input("적분 구간을 입력하세요 b : "))
n = int(input("몇 등분할지 입력하세요 n : "))
dx = (b - a) / n
x = a

def f(x):
    return x * math.exp(x)
def g(t):
    y = math.exp(t) * (t - 1)
    return y

sum = 0
for i in range(n):
    sum += f(x) * dx
    x += dx

integral = g(b) - g(a)
print("함수 te^t에 대한 구간 %.2f" % a, "부터 %.2f" % b, "까지의 적분값은 %.4f " % integral, n, "등분 했을 때의 근삿값은 %.4f" % sum, "입니다.")