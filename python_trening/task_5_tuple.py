# Кортежи

t = (5, 'программа', (1, 2))

# t[1] = 'программа'
print('t[0:3] = ', t[0:3])

# кортежи неизменяемы
# следущее действие вызовет ошибку
t[0] = 10
