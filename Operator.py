class A:
    def __init__ (self,a):
        self.a = a
    def __lt__(self,other):
        if (self.a < other.a):
            return ("Ob1 is less that Ob2")
        else:
            return ("Ob2 is less than Ob1")    
        
Ob1 = A(10)
Ob2 = A(15)
print(Ob1<Ob2)