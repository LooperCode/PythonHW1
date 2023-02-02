def fib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return fib(index-1) + fib(index-2)


index = int(input("Введите количество чисел Фибоначчи:\n"))
list = [fib(index) for index in range(1, index+2)]
print(list)
list = list[::-1] + list[1:]
for i in range(len(list)):
    if i%2 == 0 and i < len(list)//2:
        list[i] = -list[i]
print(list, '\n')
        
