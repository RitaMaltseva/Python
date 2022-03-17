per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit_rate = list(map(float, per_cent.values()))
# print(deposit_rate)
money = float(input('Введите сумму вклада: '))
sum_result = []
for i in deposit_rate:
    sum_result.append(format(i*money, '.2f'))
print(', '.join(map(str, sum_result)))
max_sum = max(sum_result)
print('Максимальная сумма, которую вы можете заработать - ', max_sum)