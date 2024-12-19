






# import pytest
# from main import sort_list
#
# def test_sort1():
#     assert sort_list([5, 6, 3, 1, 2]) == [1, 2, 3, 5, 6]
#
#
# def test_sort1():
#     assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]




# from main import is_palindrom
#
#
# def test_is_palindrom():
#     assert is_palindrom('madam') == True
#     assert is_palindrom('hello') == False
#
# @pytest.mark.parametrize("test_input,expected", [
#     ('level', True),
#     ('python', False),
#     ('racecar', True),
#     ('', True),
# ])
# def test_is_palindrom2(test_input, expected):
#     assert is_palindrom(test_input) == expected



# from main import check
#
#
# def test_check():
#     assert check(6) == True
#
# def test_check2():
#     assert check(3) == False
#
# @pytest.mark.parametrize("number, expected", [
#    (2, True),
#    (5, False),
#    (0, True),
#    (56, True),
#    (-3, False)
# ])
# def test_check_with_param(number, expected):
#     assert check(number) == expected














# import unittest
#
#
# class TestMath(unittest_TestCase):
#     def test_add(self):
#         self.assertEqual(1 + 1, 2)
#
#     def test_subtract(self):
#         self.assertEqual(3 - 2, 1)
#
#
# if __name__ == "__main__":
#     unittest.main()