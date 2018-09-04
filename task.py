"""
Type python task.py into your terminal to run the program

"""

class Check:


    def __init__(self):
        self.text = ""

    def inputString(self):
        self.text = input("Enter the String:")

      def checkString(self):
        e = []
        a = self.text
        l = len(a)
        # print(l)
        b = list(a)
        # print(b)
        for x in range(0,l,2):
            e.append(b[x])


        z = "".join(str(x) for x in e)
        print(z)

p =  Check()
p.inputString()
p.checkString()

p =  Check()
p.inputString()
p.checkString()
