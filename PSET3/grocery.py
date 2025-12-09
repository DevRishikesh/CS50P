grocery={

}
while True:
    try:
        name=input().lower()
        if name in grocery:
            grocery[name] +=1
            continue
        else:
            grocery[name] = 1

            continue
    except EOFError:
        break


for item, count in sorted(grocery.items()):
     print(f"{count} {item.upper()}")
