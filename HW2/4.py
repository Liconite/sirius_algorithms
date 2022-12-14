# Сложность: O(n)
# Пояснение: проходмся массиву и смотрим, чтобы разница
# между ценой взятого элемента и следующего в списке была равна единице

def getDescentPeriods(prices):
    dp = [1]
    for x, y in zip(prices, prices[1:]):
        # сравниваем цену x-того элемента с следующей ценой
        if x == y + 1:
            dp.append(dp[-1] + 1)
        # в случае, если цена уменьшилась больше, чем на 1, то обнуляем результат
        else:
            dp.append(1)

    return sum(dp)