#["eat", "tea", "tan", "ate", "nat", "bat"]
#result: ["eat", "tea", "ate"], \
        # ["tan", "nat"], \
        # ["bat"]

import datetime
from soupsieve.util import lower
import unittest

"""def processing_time(fun):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        fun(*args, **kwargs)
        finish = datetime.datetime.now()
        res = finish - start

        return res
    return wrapper"""

#"aaaccbdddde" -> "a3c2b1d4e1"
"""@processing_time"""
def compresed_string(string: str) -> str:

    list_letter = list(string)
    low_letters_list = list(map(lower, list_letter))


    result = []
    for i in low_letters_list:
        d = i + str(low_letters_list.count(i))
        if d not in result:
            result.append(d)
        else:
            continue

    return "".join(result)

"""print(compresed_string("AaabBccdddee"))"""















