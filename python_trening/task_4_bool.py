# Логический тип

print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False

# Можно присваивать переменным значения типа bool
# тем самым использовать переменные как средство управления (переключатель действия)

b = ('abcd')
c = ('abc')
# a = (c < b)
a = 10
if a:
    print('a = True')
else:
    print('a != True')
