def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (len(s)>=2 and len(s)<=6 and s.isalpha()):
        return True
    elif (len(s)<2):
        return False
    else:
        substring=s[2]
        if (substring=="0"):
            return False
        else:
            if (len(s)>2 and len(s)<=6 and s.isalnum()):
                return True
            
            else:
                return False

main()
