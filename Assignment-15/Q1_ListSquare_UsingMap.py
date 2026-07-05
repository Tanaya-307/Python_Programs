list_square = lambda lst : lst ** 2

def main():
    data = [1,2,3,4,5]

    print("Input data is : ",data)

    Fdata = list(filter(list_square,data))

    print("Data after filter : ",Fdata)

    Mdata = list(map(list_square,data))

    print("Data after map : ",Mdata)


if __name__=="__main__":
    main() 

    '''
    OUTPUT:
    Input data is :  [1, 2, 3, 4, 5]
    Data after filter :  [1, 2, 3, 4, 5]
    Data after map :  [1, 4, 9, 16, 25]
    '''