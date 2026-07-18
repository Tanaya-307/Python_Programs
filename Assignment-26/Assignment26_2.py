class circle:
    pi = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def accept(self):
        self.radius = float(input("Enter the value of radius : "))

    def calculateArea(self):
        self.area = circle.pi *(self.radius**2)

    def calculateCircumference(self):
        self.circumference = 2 * circle.pi * self.radius
    
    def display(self):
        print("Radius : ",self.radius)
        print("Area : ",self.area)
        print("Circumference : ",self.circumference)

print("---Object 1---")
c1 = circle()
c1.accept()
c1.calculateArea()
c1.calculateCircumference()
c1.display()

print()
print("---Object 2---")
c2 = circle()
c2.accept()
c2.calculateArea()
c2.calculateCircumference()
c2.display()

'''
OUTPUT:
---Object 1---
Enter the value of radius : 2.2
Radius :  2.2
Area :  15.197600000000003
Circumference :  13.816000000000003

---Object 2---
Enter the value of radius : 2
Radius :  2.0
Area :  12.56
Circumference :  12.56
'''
