string=str(input("Expression: "))
str=string.split()
first=float(str[0])
second=float(str[2])
if str[1]=="+":
    print(first+second)
elif str[1]=="-":
    print(first-second)
elif str[1]=="*":
    print(first*second)
elif str[1]=="/":
    print(first/second)
else:
    print("error")


