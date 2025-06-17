#this code helps to find in a list the missing numbers in the range from its min num till its max num
#данный код помогает найти пропущенные в листе цыфро в последовательности от его минимаального значения до его максимального

def which_num(l: list) -> list:
    l.sort() #we get a sorted list
    l_max = max(l)  #figure out it max number
    r = list(range(l[0], l_max + 1)) #create the whole list with all numbers
    final = [] #create an empty list where we we wll put the missing numbers

    for i in r:
        if i not in l:
            final.append(i)
    return final

print(which_num([2, 4, 1, 5, 9, 7]))
#result [3, 6, 8]


# данный код позволяет узнать можем ли мы получить первую строку из елементов второй строки
#Thia code let us to get to know if we can get the first string by the elements that the second string has

def two_strings(s_1: str, s_2: str) -> bool:
    low_letter = s_2.lower()
    list_2 = list(low_letter)
    l = []
    for i in s_1:
        if i.lower() in list_2:
            l.append(True)
        else:
            l.append(False)

    if False in l:
        return False
    else:
        return True


print(two_strings("Val", "vElery"))
#result False [it is impossible to create the first string. the second string does not have the elements tha we need for that]


