# --TASK-1
# ToDo List Application
# Create a CLI-based ToDo List app using classes.
# Define Task and ToDoList classes.
# Support adding tasks, marking as complete, listing all tasks, and listing incomplete tasks.

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.title} - {self.description} - Due: {self.due_date} - Status: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def list_all_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if not task.completed:
                print(task)


todo = ToDoList()
todo.add_task(Task("Buy groceries", "Milk, Bread, Eggs", "2025-08-01"))
todo.add_task(Task("Study Python", "Finish classes homework", "2025-08-02"))
todo.mark_task_complete(0)

print("All Tasks:")
todo.list_all_tasks()

print("\nIncomplete Tasks:")
todo.list_incomplete_tasks()

# Uzim qilmadim tan olaman internetdan oldim




# --TASK-2
# Simple Blog System
# Create a CLI-based blog system.
# Define Post and Blog classes.
# Support adding posts, listing all posts, filtering by author, editing and deleting posts.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for post in self.posts:
            print(post, "\n")

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post, "\n")

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content


blog = Blog()
blog.add_post(Post("My First Post", "Hello world!", "Ozodbek"))
blog.add_post(Post("Learning Python", "Today I learned classes.", "Ozodbek"))
blog.edit_post("My First Post", new_content="Updated content here.")
blog.delete_post("Learning Python")

print("All Posts:")
blog.list_all_posts()

print("\nPosts by Ozodbek:")
blog.posts_by_author("Ozodbek")

# Buni ham uzim qilmadim






# --TASK-3
# Simple Banking System
# Create a CLI-based banking system.
# Define Account and Bank classes.
# Support account creation, deposits, withdrawals, transfers, and overdraft handling.

class Account:
    def __init__(self, acc_no, holder_name, balance=0):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def display(self):
        print(f"Account: {self.acc_no}, Holder: {self.holder_name}, Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_no] = account

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].deposit(amount)

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].withdraw(amount)

    def check_balance(self, acc_no):
        if acc_no in self.accounts:
            print(f"Balance: {self.accounts[acc_no].balance}")

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
            else:
                print("Transfer failed: Insufficient funds.")

    def show_account(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].display()

# Example usage
bank = Bank()
bank.add_account(Account(101, "Ali", 500))
bank.add_account(Account(102, "Vali", 300))

bank.deposit(101, 200)
bank.withdraw(102, 100)
bank.transfer(101, 102, 150)

print("Account 101:")
bank.show_account(101)

print("\nAccount 102:")
bank.show_account(102)
