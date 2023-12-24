"""선택 정렬 VS 버블 정렬"""
"""Ascending"""
    
def Select(alist) :
    for i in range(1, len(alist)) :
        for j in (i + 1, len(alist) + 1) :
            if ( alist[i] > alist[j] ) :
                temp = alist[i]
                alist[i] = alist[j]
                alist[j] = temp
                
              
def Bubble(alist) :
    for i in range(len(alist) - 1) :
        for j in range(len(alist) - i - 1) :
            if ( alist[j] > alist[j + 1] ) :
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
                
    
a = [90, 10, 23, 17, 56, 39]

Select(a)
print("선택 정렬 >> ", a)

#Bubble(a)
#print("버블 정렬 >> ", a)


