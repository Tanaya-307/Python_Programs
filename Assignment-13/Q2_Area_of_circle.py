from math import pi

def Area_of_Circle(value):
    area = pi * value**2
    print("Area of Circle is : ",area)

def main():
    print("Enter the Radius of circle : ")
    Radius = float(input())

    Area_of_Circle(Radius)

if __name__=="__main__":
    main()