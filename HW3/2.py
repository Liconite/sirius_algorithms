# Cложность алгоритма: O(n)
# Пояснение: просто берём значение каждого узла и
# меняем его тип на строку. Далее просто переводим
# полученное значение в двоичную форму

def getDecimalValue(head):
    str_head = ""

    while head:
        str_head += str(head.val)
        head = head.next

    return int(str_head, 2)