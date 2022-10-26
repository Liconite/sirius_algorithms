# Cложность алгоритма: O(log n)
# Пояснение:

def sumBase(n, k):
    s = 0
    while n > 0:
        s += (n % k)
        n //= k
    return s