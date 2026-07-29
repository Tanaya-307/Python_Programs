def main():
    Filename = input("Enter Filename : ")
    search_word = input("Enter the word to search : ")

    fobj = open(Filename,"r")
    content = fobj.read()
    if search_word in content:
         print(f"The word {search_word} is found in : {Filename}")
    else:
        print(f"{search_word} not found in : {Filename}")
        
    fobj.close()


if __name__ == "__main__":
    main()

'''
OUTPUT:
1.  Enter Filename : DemoX.txt
    Enter the word to search : Ganesh
    The word Ganesh is found in : DemoX.txt

2.  Enter Filename : DemoX.txt
    Enter the word to search : Ganesh
    The word Ganesh is found in : DemoX.txt 

'''