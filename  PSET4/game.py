import random

while True:
    try:
        n=(input("Level: "))
        if n.isnumeric():
           n=int(n)
        else:
           raise Exception
        if n>=1:
            break
        else:
            continue
    except:
        pass

ran_number=random.randint(1,n)
while True:
    try:
       guess=(input("Guess: "))
       guess=int(guess)
       if guess <= 0:
            continue
       if guess==ran_number:
          print("Just right!")
          break
       elif guess>ran_number:
          print("Too large!")
          continue
       else:
          print("Too small!")
          continue
    except ValueError:
        continue













