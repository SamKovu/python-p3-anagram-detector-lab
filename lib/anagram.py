# your code goes here!

class Anagram:


    def __init__(self,word):
        self.word=word
    
    def match(self,words):
        buffer=[]

        for x in words:
           if sorted(list(x))==sorted(list(self.word)):
                buffer.append(x)
            
        return buffer



        