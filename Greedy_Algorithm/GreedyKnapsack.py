from timeit import default_timer as timer
# Structure for an item which stores weight and
# corresponding value of Item
class Item:
	def __init__(self, profit, weight):
		self.profit = profit
		self.weight = weight

# Main greedy function to solve problem
def fractionalKnapsack(W, arr):

	# Sorting Item on basis of ratio
	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True) 
	#print(arr)

	# Result(value in Knapsack)
	finalvalue = 0.0

	# Looping through all Items
	for item in arr:

		# If adding Item won't overflow, 
		# add it completely
		if item.weight <= W:
			W -= item.weight
			finalvalue += item.profit

		# If we can't add current Item, 
		# algorithm ends
		else:
			#finalvalue += item.profit * W / item.weight
			break
	
	# Returning final value
	return finalvalue


# Driver Code
if __name__ == "__main__":
	W = 300
	arr = [Item(60, 10), Item(100, 20), Item(120, 30), Item (70, 11), Item(110, 18), Item(130, 35), Item(90, 25), Item(80, 40), Item(50, 10), Item(115, 40), Item(125, 23), Item(65, 31), Item(75, 12)]
	start = timer()
    
	# Function call
	max_val = fractionalKnapsack(W, arr)
	print("Max value according to greedy algorithm:", max_val)
	
	end = timer()
	total_time = end - start
	print(total_time)