# oopl
class abc:
    def __init__(self):
        self.p = 0
        self.r = 0
        self.t = 0

    def take(self):
        self.p = int(input('Enter p:'))
        self.r = int(input('Enter r:'))
        self.t = int(input('Enter t:'))

    def si(self):
        s = (self.p*self.r*self.t)/100
        print('SI=', s)

    def ci(self):
        c = self.p*((1+(self.r/100))**self.t)-self.p
        print('CI=', c)


obj = abc()
obj.take()
obj.si()
obj.ci()
