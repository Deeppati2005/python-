class abc:
    def __init__(self):
        self.a = 0
        self.b = 0

    def take(self):
        self.a = int(input('First No:'))
        self.b = int(input('Second No:'))

    def output(self):
        c = self.a+self.b
        print('Sum=', c)


obj = abc()
obj.take()
obj.output()
