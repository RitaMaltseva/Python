# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# deposit_rate = list(map(float, per_cent.values()))
# print(deposit_rate)
# money = int(input('Введите сумму вклада: '))
# sum_result = []
# for i in deposit_rate:
#     sum_result.append(format(i*money,'.2f'))
# print(sum_result)
# max_sum = max(sum_result)
# print('Максимальная сумма, которую вы можете заработать — ', max_sum)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit_rate = list(map(float, per_cent.values()))
# print(deposit_rate)
input_money = float(input('Введите сумму вклада: '))

# объявляем переменные
deposit_sum_array = []
max_sum_value = 0
max_sum_bank_index = 0
current_bank_index = 0

# проходимся по кадому банку
for i in deposit_rate:

    # расчитаем сумму, которую ожно заработать в данном банке
    # и занесём её в массив
    bank_deposit_sum = i * input_money
    deposit_sum_array.append(bank_deposit_sum)

    # проверим, если это сумма больше максимальной,
    # то устанавливаем её как максимальную, а также записываем текущий индекс банка
    if(bank_deposit_sum >= max_sum_value):
        max_sum_value = bank_deposit_sum
        max_sum_bank_index = current_bank_index

    # увеличиваем индекс банка для следующей итерации
    current_bank_index +=1


print(deposit_sum_array)

# название банка с наивысшим значением доходности
max_sum_bank_name = list(per_cent.keys())[max_sum_bank_index]

# вывод
print('Максимальная сумма, которую вы можете заработать — ', max_sum_value, 'руб. Банк — ', max_sum_bank_name)



# max_sum = max(sum_result)
# print('Максимальная сумма, которую вы можете заработать — ', max_sum)