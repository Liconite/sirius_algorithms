# Сложность: O(n)
# Пояснение: в условии всё сказано
# (генерируем массив согласно правилам)

def getMaximumGenerated(n):
    nums = []

    for i in range(n + 1):
        if i == 0:
            nums.append(0)
        elif i == 1:
            nums.append(1)
        elif i % 2 == 0:
            nums.append(nums[i // 2])
        else:
            nums.append(nums[i // 2] + nums[(i // 2) + 1])

    return max(nums)