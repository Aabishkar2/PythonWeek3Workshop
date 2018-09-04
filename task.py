"""
Type python task.py into your terminal to run the program

"""

class Check:


    def __init__(self):
        self.text = ""
    
    def inputString(self):
        self.text = input("Enter the String:")

    def checkString(self):
        a = self.text
        e = []
        b = list(a)
        for x in b:
            if x.isdigit():
                pass
            else:
                e.append(x)

        z = "".join(str(x) for x in e)
        print(z)

p =  Check()
p.inputString()
p.checkString()

