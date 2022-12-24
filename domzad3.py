from random import uniform
numbers = []
b = int(input('Введите длину списка: '))
for i in range(b):
    numbers.append(round(uniform(0, 10),2))
print(f"Исходный список: {numbers}" )

new_lst = [round(i-int(i),2) for i in numbers]
print(new_lst)
print(max(new_lst)-min(new_lst))