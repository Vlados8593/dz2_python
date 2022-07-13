print('Реализуйте алгоритм перемешивания списка.')

llist = list(map(str, input('Введите текст через запятую --> ').split()))
index = 0
total = len(llist) // 2

while(index < total):
    llist[-1], llist[index] = llist[index], llist[-1]
    index +=1
    # 1 2 3 4 index 0
    # 4 2 3 1 index 1
    # 4 1 3 2 index 2

print('Перемешенный список --> ', llist)

