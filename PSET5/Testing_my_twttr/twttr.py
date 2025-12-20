def main():
    string=input("Enter a string" )
    shorten(string)



def shorten(word):
    vowels="aeiouAEIOU"
    newtext=""
    for c in word:
        if c not in vowels:
            newtext += c
    return newtext


if __name__ == "__main__":
    main()
