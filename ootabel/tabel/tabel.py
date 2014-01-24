'''
Created on 19.07.2013

@author: Ants Torim
'''

class Tabel(list):
    '''
    classdocs
    '''


    def __init__(self, r, c):
        '''
        Constructor
        '''
        for i in range(r): self.append([0]*c)
        

    @property        
    def freq(self):
        result = {}
        for i in range(len(self[0])):
            result[i] = {}
        for row in self:
            for i in range(len(row)):
                result[i][row[i]] = result[i].get(row[i], 0) + 1
        return result
    
    
    @property        
    def weight(self):
        result = {}
        for j in range(len(self)):
            #result[j] = {}
            result[j] = 0
            for i in range(len(self[j])):
                value = self[j][i]
                #result[j][value] = result[j].get(value, 0) + self.freq[i][value] 
                result[j] += self.freq[i][value]
        return result
   
   
class KaalutudTabel(Tabel):
    
    
    def __init__(self, r, c, kaalud):
        assert(len(kaalud)==r)
        Tabel.__init__(self, r, c)
        self.reakaalud = kaalud
        
        
             
    @property        
    def freq(self):
        result = {}
        for i in range(len(self[0])):
            result[i] = {}
        for row, kaal in zip(self, self.reakaalud):
            for i in range(len(row)):
                result[i][row[i]] = result[i].get(row[i], 0) + kaal
        return result