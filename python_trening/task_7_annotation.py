# Аннотации переменных

a: int = 5
b: str = 'строка'
c: list = [1, 2]

# Аннотация функции

def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s  # функция max возвращает максимальное значение

print(indent('123', 123))

def string_len(s: str = '') -> int:
    return len(s)

#print(string_len())

def max_list(m: list, n: list) -> int:
    return max(len(m), len(n))

print(max_list((1, 2), (3, 4, 5)))
