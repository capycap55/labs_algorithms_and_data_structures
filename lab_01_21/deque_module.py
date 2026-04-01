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
