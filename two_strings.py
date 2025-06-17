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
