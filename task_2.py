print('Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
num1 = int(input('Введите рандомное число: '))
multiplication = 1

for i in range(1, num1+1):
    print(f'Произведение чисел в заданном числе:    {i} * {multiplication} = {multiplication * i}')
    multiplication *= i

