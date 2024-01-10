class students:
    def __init__(self):
        self.n = " "
        self.r = 0
        self.m = 0

    def take(self):
        self.n = input('Enter the name:')
        self.r = (input('Enter the roll:'))
        self.m = int(input('Enter the marks:'))

    def display(self):
        print("", self.n, "\t" "", self.r, "\t" "", self.m)


l = []
for i in range(2):
    obj = students()
    obj.take()
    l.append(obj)
print("\n Name \t Roll\t Marks")
for j in l:
    j.display()
