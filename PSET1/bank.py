str=str(input("Greeting:"))
str=str.lower()
str=str.replace(" ","")
if str=="hello" or str=="hello." or str=="hello,newman":
    print("$0")
elif str=="howyoudoing?" or str=="hey" or str=="how'sitgoing?" :
    print("$20")
elif str=="what'shappening?" or str=="what'sup?":
    print("$100")
else:
    print("$1000")
