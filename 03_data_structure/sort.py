"""
    sort.py
"""

def bubble_sort(l):
    n = len(l) - 1
    for i in range(n):
        for j in range(n-i):
            if l[j] > l[j+1]:
               l[j], l[j+1] = l[j+1], l[j]
    
def select_sort(l):
    
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    
def insert_sort(l):
    pass

def quick_sort(l):
    pass

l = [2,5,1,3,7,0,9,4,8,6]
l2 = [2,5,1,3,7,0,9,4,8,6]
l3 = [2,5,1,3,7,0,9,4,8,6]
bubble_sort(l)
print(l)
select_sort(l2)
print(l2)