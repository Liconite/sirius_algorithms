# Cложность алгоритма: O(n)
# Пояснение: в условии всё сказано
# (нет, правда, в условии всё сказано)

def numberOfMatches(n):
    k_matches = 0
    while n > 1:
        if n % 2 == 0:
            k_matches += n / 2
            n /= 2
        else:
            k_matches += (n - 1) / 2
            n = ((n - 1) / 2) + 1

    return int(k_matches)