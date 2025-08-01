# users = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 17},
#     {"name": "Charlie", "age": 35},
#     {"name": "Den", "age": 15},
#     {"name": "Eve", "age": 40}
# ]

#WE HAVE TO GET A LIST WITH PEOPLE WHO ARE OVER 18 YEARS OLD

#RESULT: ["Alice", "Charlie", "Eve"]

import unittest
from unittest import TestCase


#THE FIRST WAY
def analise(lst: list) -> list:
    ages = []
    for i in lst:
        if i["age"] >= 18:
            ages.append(i["name"])
    return ages


#THE SECOND WAY
def anls(lst: list):
    ages = filter(lambda x: x["age"] >= 18, lst)
    list_name = list(map(lambda x: x["name"], ages))
    return list_name


class MyTest(TestCase):
    def test_first_def(self):
        users = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 17},
            {"name": "Charlie", "age": 35},
            {"name": "Den", "age": 15},
            {"name": "Eve", "age": 40},
            {"name": "Mark", "age": 50}
        ]

        result = analise(users)

        self.assertEqual(result, ['Alice', 'Charlie', 'Eve', 'Mark'])

        def test_second_def(self):
            users = [
                {"name": "Alice", "age": 25},
                {"name": "Bob", "age": 17},
                {"name": "Charlie", "age": 35},
                {"name": "Den", "age": 15},
                {"name": "Eve", "age": 40},
                {"name": "Mark", "age": 50}
            ]

            result = anls(users)

            self.assertEqual(result, ['Alice', 'Charlie', 'Eve', 'Mark'])

if __name__ == "__main__":
    unittest.main()








