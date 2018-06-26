

# coding: utf-8

# In[16]:

'''A queue follows FIFO (first-in, first-out). 
FIFO is the case where the first element added is the first element that can be retrieved. 
Consider a list with values [1,2,3]. Create functions queueadd and queueretrieve to add and
pop elements from the list in FIFO order respectively. After each function call, 
print the content of the list. 
Add 7 to the queue and then follow the FIFO rules to pop elements until the list is empty.'''

#  Function to add an element in to queue
def QueueAdd(lfifo,n):
    lfifo.append(n)
    
#Function to pop an element from queue in fifo order
def QueueRetrieve(lfifo):
    pop = lfifo.pop(0)
    print ('Item popped from the queue: %d '%pop)
   
  
fifo=[1,2,3]

# Extra code to add user  provided input in queue
#n=raw_input("Please enter number to add in queue ")
#n.strip()
#QueueAdd(fifo,n)

QueueAdd(fifo,7)
print ("Queue after adding element: {}\n".format(fifo))

while True:
    if fifo:
        QueueRetrieve(fifo)
        print('Remaining Queue {}\n'.format(fifo))
    else:
        print("Queue is empty")
        break

