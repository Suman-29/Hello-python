import csv

class WordCounter:
    
    def __init__(self,filename):
        fp= open(filename,'r')
        self.text= fp.read()
        self.countdict={}
        fp.close()
        
    def removepunctuation(self):
        puncList=[',','.','!','?',"'",';',':','"','/','\\','-','_','[',']','(',')','{','}']
        for punc in puncList:
            self.text = self.text.replace(punc,"")
        
        #print self.text
            
    def findcount(self):
        self.text = self.text.strip()
        self.text = " ".join(str(self.text).replace('\n',' ').replace('\r','').split())
        print (self.text)
        wordList = self.text.split(" ")
        self.countdict = {word:wordList.count(word) for word in wordList}
        #print self.countdict
          
    def writecountfile(self,csvfilename):
        
        with open(csvfilename,'w') as fp:
            wo=csv.writer(fp)
            wo.writerow(["Word", "Count"])
            for key, value in self.countdict.items():
                wo.writerow([key, value])
            print("Words and there respective counters are stored in file {}".format(csvfilename))
            
        

wordCount = WordCounter("red-headed-league.txt")

wordCount.removepunctuation()
wordCount.findcount()
wordCount.writecountfile("WordCounter.csv")

countTuple =  sorted( wordCount.countdict.items(), key=lambda x:x[1], reverse=True)
      

popularWord = [countTuple[i][0] for i in range(0,5)]
print ("Five most popular words in the file are :- {}".format(popularWord))