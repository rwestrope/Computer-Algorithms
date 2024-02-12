from DivAndConquer import binomialCoeff as simpleBiCo
from Dynamic import binomialCoef as dynamicBiCo
from timeit import default_timer as timer
import random

def set_n():
    n = random.randint(11, 20)   
    return n

def set_k():
    k = random.randint(2, 10)
    return k


#timing how long it takes divide and conquer algorithm to solve
start_simple = timer()

for i in range(1, 300):
    simpleBiCo(set_n(), set_k())

end_simple = timer()
simple_time = end_simple - start_simple
print("Simple time: ", simple_time)


#timing how long it take dynamic programming to solve
start_dynamic = timer()

for i in range(1, 300):
    dynamicBiCo(set_n(), set_k())

end_dynamic = timer()
dynamic_time = end_dynamic - start_dynamic
print("Dynamic time: ", dynamic_time)
