print('Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. '
      '\nПозиции хранятся в файле file.txt в одной строке одно число.')

total = 0
amount = int(input('\nВведите размер списка --> '))
llist = list(range(-amount,amount))
print(llist)

with open('for_task4.txt') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    print(f'Произведение {num1} элемента({llist[num1]}) с {num2} элементом({llist[num2]}) = {llist[num1]*llist[num2]}')