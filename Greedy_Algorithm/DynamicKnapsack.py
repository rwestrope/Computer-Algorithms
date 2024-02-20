from timeit import default_timer as timer
# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 


def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif wt[i-1] <= w: 
				K[i][w] = max(val[i-1] 
							+ K[i-1][w-wt[i-1]], 
							K[i-1][w]) 
			else: 
				K[i][w] = K[i-1][w] 

	return K[n][W] 


# Driver code 
if __name__ == '__main__': 
	profit = [60, 100, 120, 70, 110, 130, 90, 80, 50, 115, 125, 65, 75] 
	weight = [10, 20, 30, 11, 18, 35, 25, 40, 10, 40, 23, 31, 12] 
	W = 300
	n = len(profit)
	start = timer()
	print("Max value according to dynamic algorithm:",knapSack(W, weight, profit, n)) 
	end = timer()
	total_timer = end - start
	print(total_timer)

# This code is contributed by Bhavya Jain 
