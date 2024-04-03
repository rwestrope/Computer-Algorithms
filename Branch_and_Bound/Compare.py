from FIFO import Item, knapsack_BFS
from LeastCost import knapsack_LCS
from timeit import default_timer as timer


items = [Item(60, 10), Item(100, 20), Item(120, 30), Item (70, 11), Item(110, 18), Item(130, 35), Item(90, 25), Item(80, 40), Item(50, 10), Item(115, 40), Item(125, 23), Item(65, 31), Item(75, 12)]


FIFO_start = timer()
print(knapsack_BFS(items, 300))
FIFO_end = timer()
FIFO_time = FIFO_end - FIFO_start

f = open('FIFOOutputs.txt','a')
f.write(str(FIFO_time) + '\n')
f.close()

LC_start = timer()
print(knapsack_LCS(items, 300))
LC_end = timer()
LC_time = LC_end - LC_start

f = open('LCOutputs.txt','a')
f.write(str(LC_time) + '\n')
f.close()