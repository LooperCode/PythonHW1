from decimal import Decimal
a = Decimal(input('Введите число: '))
temp = a
if a < 0:
    a = abs(a)
s = a
b = s * 10
b %= 10
b /= 10
e = round(b, 10)
while e != int(e):
    e *= 100
e = int(e)
sumFloat = 0
while e != 0:
    sumFloat += e % 10
    e //= 10
a = int(a)
while a != 0:
    sumFloat += a % 10
    a //= 10
if temp < 0:    
    print(-sumFloat)
elif temp > 0:
    print(sumFloat)
    