a = (input("Введите номер билета: "))
sum = a[0:3]
sum2 = a[-3:]
sum = int(sum); sum2 = int(sum2)
n = 0
while sum != 0:
    n += sum % 10
    sum = sum // 10
sum = n
n = 0
while sum2 != 0:
    n += sum2 % 10
    sum2 = sum2 // 10 
sum2 = n
if sum == sum2:
    print("Билет является счастливым.")
elif sum != sum2:
    print("Билет не является счастливым.")