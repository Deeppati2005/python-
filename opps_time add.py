#add two time
class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def show(self):
        print("h: {} m: {} s: {}".format(self.h,self.m,self.s))
    def add(self,t):
        self.h+=t.h
        self.m+=t.m
        self.s+=t.s
        self.m+=self.s//60
        self.s%=60
        self.h+=self.m//60
        self.m%=60
t1=Time(10,45,30)
t2=Time(3,40,40)
t1.show()
t2.show()
t1.add(t2)
t1.show()
