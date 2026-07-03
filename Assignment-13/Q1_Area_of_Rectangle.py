def Area(V1,V2):
    area = V1 * V2
    print("Area of Rectangle is : ",area)

def main():
    print("Enter the  length of Reactangle  : ")
    Length = float(input())
    print("Enter the width of Reactangle : ")
    Width = float(input())
    Area(Length,Width)

if __name__=="__main__":
    main()