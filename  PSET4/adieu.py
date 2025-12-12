import inflect

p=inflect.engine()
listq=[]
while True:

      try:
        name=input("Name: ")

        listq.append(name)
        continue
      except EOFError:
           print("\nAdieu, adieu, to", p.join(listq[0:]))

           break



