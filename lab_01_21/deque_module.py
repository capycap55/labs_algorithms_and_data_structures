# Задание task_21. Реализация модуля Дек.  Проверка на палиндром с использованием двухсторонней очереди.
# Выполнил: Попова С.Е.
# Группа: ЦИБ-251
# Сложность алгоритма - O(n)
class Node:
    """Узел двусвязного списка"""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque: #Дек на основе двусвязного списка
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def add_front(self, item): #Добавление в начало
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    def add_back(self, item): #Добавление в конец
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def remove_front(self): #Удаление из начала
        if self.head is None:
            raise IndexError("remove_front from empty deque")
        data = self.head.data        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return data
    def remove_back(self): #Удаление из конца
        if self.tail is None:
            raise IndexError("remove_back from empty deque")
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return data
    def size(self): #Количество элементов
        return self.length
    def is_empty(self): #Проверка на пустоту
        return self.length == 0
