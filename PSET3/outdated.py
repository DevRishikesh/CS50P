month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#new_get=""

while True:
    try:
        get=input("Date: ")
        if "/" in get:
            new_get=get.split('/')
            mm,dd,yy=int(new_get[0]),int(new_get[1]),int(new_get[2])
            if mm<=12 and dd<=31:
               print(f"{yy}-{mm:02}-{dd:02}")
               break
            else:
                continue
        else:
            new_get=get.split()
            mm,dd,yy=(new_get[0]),(new_get[1]),int(new_get[2])
            if "," in dd:
                dd=int(dd.replace(",",""))
            else:
                continue
            if mm.title() in month and dd<=31:
               mm=month.index(mm.title())+1
               print(f"{yy}-{mm:02}-{dd:02}")
               break
            else:
                continue



    except EOFError :
           break








