# Python program to find number of bins required using
# First Fit Decreasing algorithm.

# Returns number of bins required using first fit
# online algorithm
def firstFit(weight, n, c):
	
	# Initialize result (Count of bins)
	res = 0
	
	# Create an array to store remaining space in bins
	# there can be at most n bins
	bin_rem = [0]*n
	
	# Place items one by one
	for i in range(n):
	
		# Find the first bin that can accommodate
		# weight[i]
		j = 0
		while( j < res):
			if (bin_rem[j] >= weight[i]):
				bin_rem[j] = bin_rem[j] - weight[i]
				break
			j+=1
			
		# If no bin could accommodate weight[i]
		if (j == res):
			bin_rem[res] = c - weight[i]
			res= res+1
	return res
	
# Returns number of bins required using first fit
# decreasing offline algorithm
def firstFitDec(weight, n, c):

	# First sort all weights in decreasing order
	weight.sort(reverse = True)

	# Now call first fit for sorted items
	return firstFit(weight, n, c)

# Driver program
weight = [ 2, 5, 4, 7, 1, 3, 8 ]
c = 10
n = len(weight)
print("Number of bins required in First Fit Decreasing : ",str(firstFitDec(weight, n, c)))

# This code is contributed by shinjanpatra
