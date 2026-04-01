# Задание task_21. Основной скрипт. Проверка на палиндром с использованием двухсторонней очереди.
# Выполнил: Попова С.Е.
# Группа: ЦИБ-251
# Сложность алгоритма - O(n**2), т.к. операция добавления и удаления элемента в начало списка при реализации дека имеет сложность O(n)

from deque_module import Deque
def is_palindrome(s):
  d = Deque()

  for ch in s:
    d.add_back(ch) # добавление элементов строки в дек

  while d.size() > 1:
    front = d.remove_front()
    back = d.remove_back()

    if front != back:
      return False

  return True # проверка на палиндром

word_is_palindrome = "шалаш"
print(is_palindrome(word_is_palindrome)) # проверка, является ли палиндром палиндромом; возвращает True
word_is_not_palindrome = "кружок"
print(is_palindrome(word_is_not_palindrome)) # проверка, является ли не палиндром палиндромом; возвращает False
check = input()
print(is_palindrome(check)) # проверка, является ли введённая строка палиндромом
