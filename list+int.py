def two_num(lst: list, num: int):
    if num == 1: #we do this check becouse anyway there will not be any numbers to get 1 (it is already ==1)
       return "Enter another number"
    a = lst  #we create two lists in order to run through each of them and to try to sum every numbers from the one list with onother one
    b = lst
    for num_a in a: #we take one element from the first list
        for numb_b in b: #then we take each element from the second list
            if numb_b + num_a == num: #and make checking
                s = [num_a, numb_b]
                if numb_b == num_a: #in this case we can make conclusion that we have checked every numbers and now only one case left to sum two equel numbers
                    f = "there are no such numbers"
                    return f
                else:
                    return s

print(two_num([1, 2, 3, 4, 5], 10))