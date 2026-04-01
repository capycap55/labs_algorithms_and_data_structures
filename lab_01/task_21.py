# Задание task_21.
# Выполнил: Попова С.Е.
# Группа: ЦИБ-251

class Deque:
  def __init__(self):
    self.items = [] # создание пустого списка для хранения элементов дека

  def add_front(self, item):
    self.items.insert(0, item) # добавление элемента в начало списка

  def add_back(self, item):
    self.items.append(item) # добавление элемента в конец списка

  def remove_front(self):
    return self.items.pop(0) # удаление элемента в начале списка

  def remove_back(self):
    return self.items.pop() # удаление элемента в конце списка

  def size(self):
    return len(self.items) # количество элементов в списке

def is_palindrome(s):
  d = Deque()

  for ch in s:
    d.add_back(ch) # добавление элементов строки в список

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
check = str(input())
print(is_palindrome(check)) # проверка, является ли введённая строка палиндромом
