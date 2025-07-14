# n = 19: (1**2 + 9**2 = 82)
# n = 82: (8**2 + 2**2 = 68)
# n = 68: (6**2 + 8**2 = 100)
# n = 100: (1**2 + 0**2 + 0**2 = 1)
# True

import unittest

def num_num(num: int) -> bool | None:
    l_1 = []
    l_set = set(l_1)

    while num != 0: #just we do that in order to repeat the action again and again (till we get the result) Kind of "for"

        if len(l_1) != len(l_set): #we check it because if there is some repetition then it will go on the circle. in this case 100% we will never get 1
            return False
        else:
            v = num
            num_list = list(str(v)) #we get a list with numbers
            l = list(map(lambda x: int(x) ** 2, num_list)) #using lambda every number in the list we turn into x**2

            if sum(l) == 1:
                return True
            else:
                num = sum(l)
                l_1.append(sum(l))
                l_set = set(l_1)

print(num_num(2))
#with 2 it is False





