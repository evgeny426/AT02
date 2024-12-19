import pytest
from main_hw import count_russian_vowels


# Тесты для функции count_russian_vowels
def test_only_vowels():
    """Проверяем, что функция правильно считает гласные в строке, содержащей только гласные."""
    assert count_russian_vowels("аеёиоуыэюя") == 10
    assert count_russian_vowels("АЕЁИОУЫЭЮЯ") == 10
    assert count_russian_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ") == 18

def test_no_vowels():
    """Проверяем, что функция возвращает 0 для строки, не содержащей гласных."""
    assert count_russian_vowels("бвгджзйклмнпрстфхцчшщ") == 0
    assert count_russian_vowels("1234567890") == 0
    assert count_russian_vowels("!@#$%^&*()") == 0

def test_mixed_case():
    """Проверяем, что функция правильно считает гласные в смешанных строках (с прописными и строчными буквами)."""
    assert count_russian_vowels("Привет") == 2
    assert count_russian_vowels("Как дела?") == 3
    assert count_russian_vowels("Это ТЕСТ") == 2
    assert count_russian_vowels("аБвГдЕёЖзИйКлМнОпрСтУфХцЧшЩъЫьЭюЯ") == 10

def test_empty_string():
    """Проверяем, что функция возвращает 0 для пустой строки."""
    assert count_russian_vowels("") == 0