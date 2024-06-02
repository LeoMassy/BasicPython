a = 61
b = 10

# TODO
a = 61
if num <= 1:
    print(False)
else:
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            print(False)
            break
    else:
        print(True)
    
    
    b = 10

if b <= 1:
    print(False)
else:
    for i in range(2, int(b**0.5)+1):
        if b % i == 0:
            print(False)
            break
    else:
        print(True)
    
    
