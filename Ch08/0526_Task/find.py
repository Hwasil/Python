'''
0526
p273_8_3_1 모듈
'''

def findMax(a,b,c) :
    if a>b :
        biggest=a
    else :
        biggest=b
    if biggest<c :
        biggest=c
    
    return biggest

def findMin(a,b,c) :
    if a>b :
        smallest=b
    else :
        smallest=a
    if smallest>c :
        smallest=c
    return smallest

def findSum(a,b,c) :
    return a+b+c