def main():
    

    try : 
        fobj = open("demo.txt","w")
        print("File gets opened")

        fobj.write("Marvellous infosystems")

        fobj.close

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__=="__main__":
    main()