numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

# Ищем индекс пропущенного элемента
index_of_none = numbers.index(None)

# Находим среднее арифметическое значение
sum_of_numbers = sum(numbers[:index_of_none]) + sum(numbers[index_of_none + 1:])
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers

# Замена значения пропущенного элемента средним арифметическим
numbers[index_of_none] = average_of_numbers

print("Измененный список:", numbers)
