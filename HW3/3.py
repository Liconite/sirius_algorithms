# Cложность алгоритма: O(n)
# Пояснение: проходимся по значениям на одном уровне,
# суммиуем их и делим на их кол-во

def averageOfLevels(root):
    stack = [root] # записывем значение корня в стэк
    res = []
    while stack: # проходимся по стэку
        tem = []
        value = 0 # создаём счётчик
        for i in stack:
            if i.left: # проверка на значение слевой стороны
                tem.append(i.left)
            if i.right: # проверка на значение справой стороны
                tem.append(i.right)
            value += i.val # суммируем значения
        res.append(value / len(stack)) # сохраняем значение в список
        stack = tem[:]
    return res