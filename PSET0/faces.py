str=str(input())
good=str.find(")")
bad=str.find("(")
if (good!=-1) and (bad==-1):
    print("Hello 🙂")
elif (bad!=-1) and (good==-1):
    print("Goodbye 🙁")
else:
    print("Hello 🙂 Goodbye 🙁 ")
