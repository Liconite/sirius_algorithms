# Cложность алгоритма: O(n)
# Пояснение: восстанавливаем последовательность по заданному правилу

def tribonacci(n):
    t = [0, 1, 1] + [0] * 35  # список для записи значений (первые три значения нам известны из условия)

    for i in range(3, n + 1):
        t[i] = t[i - 1] + t[i - 2] + t[i - 3]  # восстанавливаем элемент последовательности по правилу

    return t[n]
