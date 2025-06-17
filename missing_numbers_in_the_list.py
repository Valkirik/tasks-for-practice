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





