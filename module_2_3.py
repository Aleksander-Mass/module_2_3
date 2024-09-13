my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# 2. Напишите цикл while с соответствующими задаче условиями

i = 0  # счетчик цикла

print('Исходный список: ', my_list)

while i <= len(my_list):
    if my_list[i] < 0:
        break

    if my_list[i] > 0:
        print(my_list[i])

        if my_list[i] == 0:
            continue

    i = i + 1