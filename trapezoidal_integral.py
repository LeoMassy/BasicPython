from math import sin
from math import pi
a = 0
b = pi / 2
n = 100
h = (b - a) / n
x = 0

for i in range(n):
    x += h * (sin(a + h * i) + sin(a + h * (i + 1))) / 2
print(x)