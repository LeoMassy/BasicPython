a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
r = a % b

while(r != 0):
   a,b = b,a%b
else:
    print('最大公約数は{}'.format(b))



