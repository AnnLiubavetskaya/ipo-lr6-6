import random
count =  0 
unik = []
list1 = []
your_num = int(input("Введите число для сравнения: "))

for i in range(20):
    list = [random.randint(-10,10) for a in range(4)]
    list1.append(list)

for i in list1 :
    if i not in unik:
        unik.append(i)

for i in list1:
    if sum(i) < your_num:
        count += 1

print(f"Уникальные значения списка: {(tuple(unik))}")
print(f"Cчетчик комбинаций,сумма которых меньше,чем введенное число {your_num}: {count}")



 