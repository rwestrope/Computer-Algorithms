import sys
import math
from timeit import default_timer as timer
sys.setrecursionlimit(10**8)

c = 0
def knapSack(mW,w,v,n):
    # counter how many time recursive function is called.
    global c
    c += 1
    
    if(mW == 0 or n == 0):
        return [0,[]]
        
    if(w[n-1] > mW):
        return knapSack(mW,w,v,n-1)
        
    set1 = knapSack(mW-w[n-1],w,v,n-1)
    set2 = knapSack(mW,w,v,n-1)
    
    if(set1[0]+v[n-1] > set2[0]):
        set1[1].append(n-1)
        set1[0] += v[n-1]
        return set1
    else:
        return set2
        
val = [60, 100, 120, 70, 110, 130, 90, 80, 50, 115, 125, 65, 75] 
wt = [10, 20, 30, 11, 18, 35, 25, 40, 10, 40, 23, 31, 12]
W = 300
n = len(val)

start = timer()
print("Max value (and list) according to backtracking algorithm:",knapSack(W, wt, val, n))
end = timer()

print("Total time:",end-start)
#print("Total Recursive Steps: ",c)