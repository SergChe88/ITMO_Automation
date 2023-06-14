# определяем функцию
def add(x, y):  # add - уникальное имя функции
    return x + y  # нельзя использовать последовательно два return, но можно использовать условие

# вызываем функцию
add(1, 2)
print(add(1, 2))
# через переменную
# f = add(1, 2)
# print(f)

print(add('I am', ' tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))

# print(arg(2, 2))

# print(arg(2, 2, '1', 1))

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))


def single(x=(1, 2, 3, 4)):
    return x[0]

def double(radius, pi=3.14159):
    return pi*(radius**2)

print(single())
# print(double(10)
