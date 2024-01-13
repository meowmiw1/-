# Чтение данных из входного файла
with open('input.txt', 'r') as file:
    temperatures = list(map(int, file.readline().split()))

# Расчет среднесуточной температуры
average_temperature = sum(temperatures) / len(temperatures)

# Запись результата в output
with open('output.txt', 'w') as file:
    file.write(str(average_temperature))

# Закрытие файлов
file.close()
