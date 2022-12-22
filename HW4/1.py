# Cложность алгоритма: O(nlog(n))
# Пояснение: Ключевым алгоритмом этой задачи является
# распределение людей на 2 равные группы в 2 города при меньшей с стоимостью перелёта.


def twoCitySchedCost(costs):
    diffs = []
    for c1, c2 in costs:
        diffs.append([c2 - c1, c1, c2])  # узнаём разницу и записываем в массив
    diffs.sort()

    res = 0
    for i in range(len(diffs)):
        if i < len(diffs) // 2:
            res += diffs[i][2]  # отправляем в город A
        else:
            res += diffs[i][1]  # отправляем в город Б
    return res
