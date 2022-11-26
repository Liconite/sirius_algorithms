# Сложность: O(n*m)

def uniquePathsWithObstacles(obstacleGrid):
    # узнаём размерность поля
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    # создаём пустое поле
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # заполняем всю строку 1, так это одно из двух возможных направлений движения
    for i in range(n):
        if obstacleGrid[0][i] == 1:
            break
        dp[0][i] = 1

    # делаем тоже самое со столбцом
    for j in range(m):
        if obstacleGrid[j][0] == 1:
            break
        dp[j][0] = 1

    # считаем количество возможных путей в выбранной клетке
    for j in range(1, m):
        for i in range(1, n):
            if obstacleGrid[j][i] == 1:
                continue
            dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

    return dp[-1][-1]