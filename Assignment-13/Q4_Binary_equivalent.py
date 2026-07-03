def BinaryEquivalent(No):
    BinaryValue = 0
    PlaceValue = 1
    while (No > 0):
        remainder = No % 2
        BinaryValue = BinaryValue + (remainder * PlaceValue) #builds binary  number
        No = No // 2
        PlaceValue = PlaceValue * 10 
    return BinaryValue
    
def main():
    print("Enter the Number : ")
    Number = int(input())

    ret = BinaryEquivalent(Number)
    print("Binary equivalent = ",ret)

    
if __name__=="__main__":
    main()

    '''
OUTPUT:

Enter the Number :
10
Binary equivalent =  1010

    '''