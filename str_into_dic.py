#"Python is great, and python is easy. Isn't it great?" -> {'python': 2, 'is': 2, 'great': 2, 'and': 1, 'easy': 1, 'isnt': 1, 'it': 1}

def str_into_dic(string: str) -> dict:
    signs = "!?.,:;'"

    list_str = list(string)
    new_list = [i for i in list_str if i not in signs]
    new_str = "".join(new_list).lower()

    f = new_str.split(" ")
    data = {}

    for i in f:
        data[i] = f.count(i)

    return data

print(str_into_dic("Python is great, and python is easy. Isn't it great?"))
