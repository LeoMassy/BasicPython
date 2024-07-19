import math

def trapezoidal_integral(f, a=0, b=1, n=100):
    # 区間幅
    h = (b - a) / n
    # 台形の面積を計算
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

# (1) sin⁡x を区間 [0,π/2] で台形積分 (n=50)
def func1(x):
    return math.sin(x)

result1 = trapezoidal_integral(func1, 0, math.pi / 2, 50)
print(f"(1) sin(x) on [0, π/2] with n=50: {result1}")

# (2) 4/(1+x^2) を区間 [0,1] で台形積分 (n=100)
def func2(x):
    return 4 / (1 + x ** 2)

result2 = trapezoidal_integral(func2, 0, 1, 100)
print(f"(2) 4/(1+x^2) on [0, 1] with n=100: {result2}")

# (3) √(π)exp⁡(−x^2) を区間 [−100,100] で台形積分 (n=1000)
def func3(x):
    return math.sqrt(math.pi) * math.exp(-x ** 2)

result3 = trapezoidal_integral(func3, -100, 100, 1000)
print(f"(3) √(π)exp(−x^2) on [−100, 100] with n=1000: {result3}")
