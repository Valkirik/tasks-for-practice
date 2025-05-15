def the_same(lst: list) -> int:
    "преобразуем в set чтобы удалить повторяющиеся элементы"
    set_list = list(set(lst))
    "списокб в который будем закидывать те повторяющиеся элементы (не включая оригинал цыфры)"
    num = []
    "пробегаемся по листу"
    for i in lst:
        if i not in set_list:
            num.append(i)
            var = ("удаляем номер из сокращенного листа,/"
                   "чтобы оригиналиный лист не смог уже сравнивать/"
                   "повторяющиеся элементы с не существующими уже в сэте")
        else: set_list.remove(i)


    "создаем список из такого же количества элементов сколко повторяющихся. в нашем случае 3: 3, 4 и 5"
    new_list = []
    for i in list(set(num)):
        if i:
            var = ("добавляем в новый список нули чтобы/"
             "их подставить потом в качестве/"
             "значений ключей чтобы подсчитывать/"
             "количестыо каждого")
            new_list.append(0)


    "содзаем словарь {3: 0, 4: 0, 5: 0}"
    dictionary = dict(zip(list(set(num)), new_list))
    "подсчитываем количество каждого ключа"
    for num_1 in num:
        for i in dictionary.keys():
            "если значение ключа совпадает со значением в списке где все повторяющиеся элементы"
            if num_1 == i:
                dictionary[i] += 1


    set_list = list(set(lst))
    if len(lst) > len(set_list):
        final = len(lst) - len(set_list)
        return f"There are {final} repeatitions: {dictionary}"
    else:
        str = "the list does not have repeated numbers"
        return str

print(the_same([1, 2, 3, 3, 4, 4, 5, 5, 3, 3]))



























