'''
Created on 16.07.2013

Good one?

@author: Ants Torim
'''

def naive_zeros(n, m):
    return [[0]*n]*m

def zeros(n, m):
    result = []
    for i in range(m):
        result.append([0]*n)
    return result


def freq(table):
    result = {}
    for i in range(len(table[0])):
        result[i] = {}
    for row in table:
        for i in range(len(row)):
            result[i][row[i]] = result[i].get(row[i], 0) + 1
    return result

if __name__ == '__main__':
    t = naive_zeros(5,8)
    t[0][ 0] = 1
    print(t)
    t = zeros(5,8)
    t[0][ 0] = 1
    print(freq(t))