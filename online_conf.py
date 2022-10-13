quantity_of_ticket = int(input('Введите количество билетов '))
age = []
cost = []
for i in range (1, quantity_of_ticket + 1): #запрашиваем возраст
    age.append(int(input('Введите возраст ')))

for j in range (quantity_of_ticket): #проверяем соответствие условиям заполняем список значений стоимости
    if age[j] < 18:
        cost.append(0)
    elif 18 <= age[j] < 25:
        cost.append(990)
    else:
        cost.append(1390)

summary_cost = sum(cost)
print('Общая стоимость:', summary_cost)
if 3 < quantity_of_ticket: #проверяем соответствие условиям на скидку
    summary_cost *= 0.9
    print('Общая стоимость со скидкой 10%:', int(summary_cost))