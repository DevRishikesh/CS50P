from bank import value

def test_bank():
     zero=["Hello","Hello.","Hello, newman"]
     one=["How you doing?","hey","how's it going?"]
     two=["What's Happening?","What's up?"]
     three=["Nothing"]
     for i in zero:
          assert value(str(i)) == 0
     for j in one:
          assert value(str(j)) == 20
     for k in two:
          assert value(str(k))  == 100
      