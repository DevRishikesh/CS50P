print("What is the Answer to the Great Question of Life, the Universe, and Everything?")
ans=input()
ans=ans.replace(" ","")
ans=ans.replace("-","")
ans=ans.lower()
if (ans=="42" or ans=="fortytwo"):
    print("Yes")
else:
    print("No")
