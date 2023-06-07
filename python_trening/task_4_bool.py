# Логический тип

print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False

# Можно присваивать переменным значения типа bool
# тем самым использовать переменные как средство управления (переключатель действия)

b = ('abcd')
c = ('abc')
a = (c < b)
# ещё варианты
# a = 0  #False
# a = 1 или a = -1 #True
# a = 'a' #True
# a = '' #False
if a:
    print('a = True')
else:
    print('a != True')
