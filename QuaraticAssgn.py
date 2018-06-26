class Quadratic: 
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.equation=''           
        
    def __add__(self,other):
        d = self.a + other.a
        e = self.b + other.b
        f = self.c + other.c 
        #return self._createEquation__(d,e,f)
        return Quadratic(d,e,f)      

    
    def __sub__(self,other):
        d = self.a - other.a
        e = self.b - other.b
        f = self.c - other.c
       # return self._createEquation__(d,e,f)
        return Quadratic(d,e,f) 

        
    def __eq__(self,other):
        if  self.a == other.a:
            if  self.b == other.b:
                if  self.c == other.c:
                    return True
        return False            
                    
    def _createEquation__(self,a,b,c):
        #It's a 
        if a==0:
            temp=''
        elif a==1:
            temp ='x^2'
        else:
            temp =str(a)+'x^2'
            
        if b>0 and b!=1:
            temp+='+'+str(b)+'x'
        elif b<0:
            temp+=str(b)+'x'
        elif b==1:
            temp+='+x'
            
        if c>0:
            temp+='+'+str(c)
        elif c<0:
            temp+=str(c)
        self.equation = temp
        return temp
    def __str__(self):
        return '%d x^2 + %d x + %d' %(self.a,self.b,self.c)    
        
    
Q1 = Quadratic(3,8,-5)
Q2 = Quadratic(2,3,7)  

quadAdd = Q1+Q2
print (quadAdd)

quadSub = Q1-Q2
print (quadSub)

if Q1==Q2:
    print ("The two quadratic expressions are equal")
else:
    print ("The two quadratic expressions are not equal")

