class Bookstore:
    NoofBooks = 0

    def __init__(self,name,author):
        self.name = name
        self.author = author

        Bookstore.NoofBooks = Bookstore.NoofBooks+1

    def display(self):
        print(f"print {self.name} by {self.author}")
        print("No. of Books :",Bookstore.NoofBooks)

obj1 = Bookstore("Linux system programming","Robert Love")
obj1.display()

print()
obj2 = Bookstore("C programming","Dennis Ritchie")
obj2.display()

'''
OUTPUT:
print Linux system programming by Robert Love
No. of Books : 1

print C programming by Dennis Ritchie
No. of Books : 2
'''