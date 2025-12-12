import random


def main():
    score=0
    l=get_level()
    for _ in range(10):
           j=0
           x1=generate_integer(l)
           y1=generate_integer(l)
           while True:
             try:
                 if j<3:
                   guess=input(f"{x1} + {y1} = ")
                   guess=int(guess)
                   tot=int(x1)+int(y1)
                   if guess==tot:
                       score+=1

                       break
                   else:
                       j+=1
                       print("EEE")
                       continue
                 else:
                     print(f"{x1} + {y1} = {x1+y1}")

                     j-=3
                     break
             except ValueError:
                    j+=1
                    print("EEE")
                    continue
    print(f"Score: {score}")



def get_level():
    while True:
       try:
        get_n=input("Level: ")
        get_n=int(get_n)
        if 1<=get_n and get_n<=3:
            level_n=get_n
            return level_n
            break
        else:

            continue
       except ValueError:
           continue

def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)










if __name__ == "__main__":
    main()
