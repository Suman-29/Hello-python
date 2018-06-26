
# coding: utf-8

# In[17]:

class InterestCalculator(object):
    '''This is a parent class InterestCalculator'''
    def __init__(self,years,rate,principal):
        self.years=years
        self.rate=rate
        self.principal=principal
        self.interest = 0
        
class CICalculator(InterestCalculator):
    '''Compound Interset final amount formula is P(1+r/100)**n'''
    def calcfinalval(self):
        self.interest = (self.principal*((1+self.rate)**self.years))-self.principal
        self.finalval = self.principal+self.interest

    
class SICalculator(InterestCalculator):
    '''Simple Interest final amount is P(1+rn)'''
    def calcfinalval(self):
        self.interest= (self.principal* self.rate*self.years )
        self.finalval = self.principal + self.interest
        
c = CICalculator(1,0.1,1100)
c.calcfinalval()
print "Final amount after applying compound interest is ", c.finalval

s = SICalculator(1,0.1,1000)
s.calcfinalval()
print "Final amount after applying simple interest is ", s.finalval

print ("\n----------------------------------------------------------")

# In[18]:


# Question 2: 5 points
'''A stack follows LIFO (last-in, first-out). LIFO is the case where the last 
element added is the first element that can be retrieved. 
Consider a list with values [4,6,9]. Create a class called Sclass with 
functions sadd and sretrieve to add and pop elements from the list 
in LIFO order respectively. After each function call, print the contents 
of the list. Add 12 to the stack and then follow the LIFO rules and 
pop elements until the list is empty.'''


class Sclass(object):
    '''Its a Stack class which follows LIFO(Last In first out)'''
    def __init__(self,list1):
        self.stack=list1[:]
    #  Function to add an element in to stack
    def s_add(self,n):
        (self.stack).append(n)
    
    #Function to pop an element from stack in lifo order
    def s_retrieve(self):
        pop = (self.stack).pop(-1)
        print ('Item popped from the stack: %d '%pop)
   
  
list1=[4,6,9]

st1= Sclass(list1)
st1.s_add(12)

print ("Updated Stack after adding element: {}\n".format(st1.stack))

while True:
    if st1.stack:
        st1.s_retrieve()
        print('Remaining stack after popping element{}\n'.format(st1.stack))
    else:
        print("Stack is empty")
        break


