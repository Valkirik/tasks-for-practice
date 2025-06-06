# "Hello everyone my name is Valera" -> "Valera is name my everyone Hello"
#This function let us reverse any strings.\
#Even if we have a few spaces between words,\
#in the end we get the string with only one space between them

#Данная функция позволяет нам переворачивать любую строкую \
# Даже если у нас несколько пробулов между словами, \
#в конце мы получаем строку только с одним пробелом мжду ними

def my_reverse(string: str) -> str:
    word_list = string.split(" ") #turning into a list (separated by words)
    word_list.reverse() #reversing in
    list_without_space = [] #creating an empty list
    for i in word_list:
        if i != '':
            list_without_space.append(i) #using this checking we are deleting the spare spaces
    str_new = " ".join(list_without_space) #joing final list
    return str_new


print(my_reverse("Valera  is   name my   everyone    Hello"))

