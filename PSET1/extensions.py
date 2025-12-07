str=str(input("File name: ")).lower().strip()
if str.endswith(".gif") or str.endswith(".jpg") or str.endswith(".jpeg") or str.endswith(".png") :
    print("image/"+str.split(".")[-1])
elif str.endswith(".pdf"):
    print("application/pdf")
elif str.endswith(".txt"):
    print("text/plain")
elif str.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
