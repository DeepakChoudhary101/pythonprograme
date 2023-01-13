class swap:
        def getData(self,x,y):
            self.a=x;
            self.b=y
        def putData(self):
            self.a,self.b=self.b,self.a
        def display(self):
            print("a:=",self.a)
            print("b=",self.b)
            print("gd")
k=swap()
k.getData(12,33)
k.display()
k.putData()
k.display()