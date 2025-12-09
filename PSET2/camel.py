name=str(input("camelCase: "))
i=0
new=""
while i < len(name):
    if (name[i].isupper()):
        new=new+"_"+name[i].lower()
    else:
        new=new+name[i]

    i+=1

print("snake_case:",new)

