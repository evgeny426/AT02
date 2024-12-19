import sqlite3


def init_db():
   conn = sqlite3.connect(':memory:')
   cursor = conn.cursor()
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   name TEXT,
   age INTEGER)
   ''')
   return conn

# def sort_list(numbers):
#     return sorted(numbers)


# def is_palindrom(s):
#     return s == s[::-1]




# def check(number):
#    return number % 2 == 0
#
#
#
#
# # import pytest
# #
# #
# # def test_add2():
# #     assert 1 + 1 == 2
# #
# # def test_subtract():
# #     assert 3 - 2 == 1