immutable_var = (21, '09', 24, 'kayaks')
#immutable_var[3] = 'rafting'
print(immutable_var)
#Компилятор выдает ошибку, потомучто переменная immutable_var содержит кортеж (tuple) - неизменяемые объекты

mutable_list = [22, 9, 24, 'shell']
mutable_list[1] = '09'
print(mutable_list)