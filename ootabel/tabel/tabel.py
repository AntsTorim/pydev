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