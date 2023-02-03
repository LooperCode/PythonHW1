import random
def rndCoin (n):
    count = 0
    for i in range(n):
        a = random.randint(0, 1)
        if a == 0:
            count += 1
        print(a, end=' ')
    print('\n')         
    return count 


n = int(input(("Введите кол-во монеток: ")))
print(rndCoin(n))
