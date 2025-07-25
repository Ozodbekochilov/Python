# --TASK-1
# Circle class with area and perimeter methods

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())



# --TASK-2
# Person class with age calculation

from datetime import date

class Person:
    def __init__(self, name, country, birth_date):  # birth_date in format: (YYYY, MM, DD)
        self.name = name
        self.country = country
        self.birth_date = date(*birth_date)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

p = Person("Alice", "USA", (2000, 5, 20))
print("Age:", p.get_age())



# --TASK-3
# Calculator class with basic operations

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "Cannot divide by zero"

calc = Calculator()
print("Add:", calc.add(3, 2))
print("Divide:", calc.divide(10, 0))



# --TASK-4
# Shape base class and subclasses Circle, Triangle, Square

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):  # triangle sides
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):  # Heron's formula
        s = self.perimeter() / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
    
sq = Square(4)
print("Square Area:", sq.area())



# --TASK-5
# Binary Search Tree class

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def _insert(node, data):
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            else:
                node.right = _insert(node.right, data)
            return node

        self.root = _insert(self.root, data)

    def search(self, value):
        def _search(node, value):
            if node is None or node.data == value:
                return node
            if value < node.data:
                return _search(node.left, value)
            return _search(node.right, value)

        return _search(self.root, value)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print("Found:", bst.search(5) is not None)



# --TASK-6
# Stack class

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value): self.stack.append(value)
    def pop(self): return self.stack.pop() if self.stack else None

s = Stack()
s.push(1)
s.push(2)
print("Popped:", s.pop())



# --TASK-7
# Linked List class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete(self, key):
        cur = self.head
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if not cur:
            return
        if prev:
            prev.next = cur.next
        else:
            self.head = cur.next

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.delete(10)
ll.display()



# --TASK-8
# Shopping Cart class

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

cart = ShoppingCart()
cart.add_item("Book", 15)
cart.add_item("Pen", 5)
print("Total:", cart.total_price())



# --TASK-9
# Stack with push, pop, display

class StackDisplay:
    def __init__(self):
        self.items = []

    def push(self, val): self.items.append(val)
    def pop(self): return self.items.pop() if self.items else None
    def display(self): print("Stack:", self.items)

sd = StackDisplay()
sd.push(5)
sd.display()
sd.pop()
sd.display()



# --TASK-10
# Queue class

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val): self.queue.append(val)
    def dequeue(self): return self.queue.pop(0) if self.queue else None

q = Queue()
q.enqueue(1)
q.enqueue(2)
print("Dequeued:", q.dequeue())



# --TASK-11
# Bank class for managing accounts and transactions

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_amount=0):
        self.accounts[name] = initial_amount

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount

    def balance(self, name):
        return self.accounts.get(name, "Account not found")
bank = Bank()
bank.create_account("John", 100)
bank.deposit("John", 50)
print("Balance:", bank.balance("John"))
