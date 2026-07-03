def chkvowel(Char):
    if Char in "aeiou":
        print(Char,"is a Vowel")
    else:
        print(Char,"is a consonant")

def main():
    ch = input("Enter the character : ")
    chkvowel(ch)

if __name__=="__main__":
    main()
