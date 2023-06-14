# Задача №1
def task_1() -> str:
    i: int = 10
    f: float = 3.14
    s: str = "Hello, world!"
    l: list = [1, 2, 3, 4, 5]
    b: bool = True
    return print(' type i - ', type(i),'\n','type f - ',type(f),'\n','type s - ',type(s),'\n','type l - ',type(l),'\n','type b - ',type(b),'\n')
task_1()

# Задача №2
def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return print(a[0:3])
task_2()
# *список

# Задача №3
def task_3() -> float:
    print("Введите число")
    val: float = float(input())
    return val * val

print("Квадрат числа - ", task_3())
