import random
from timeit import default_timer as timer
from MergeSort import mergeSort
from QuickSort import quickSort

data_one = []
data_two = []
data_three = []
data_four = []
data_five = []

all_data = [data_one, data_two, data_three, data_four, data_five]


for data_group in all_data:
    for i in range(0, 10):
        n = random.randint(-1000, 1000)
        data_group.append(n)


start_merge = timer()

for data_group in all_data:
    arr_length = len(data_group)
    mergeSort(data_group, 0, arr_length-1)

end_merge = timer()
merge_time = end_merge - start_merge
print(f"Merge Sort time: ", merge_time)



start_quick = timer()

for data_group in all_data:
    arr_length = len(data_group)
    quickSort(data_group, 0, arr_length-1)

end_quick = timer()
quick_time = end_quick - start_quick
print(f"Quick Sort time: ", quick_time)

if quick_time > merge_time:
    print("Merge Sort was faster.")
elif merge_time > quick_time:
    print("Quick Sort was faster.")
else:
    print("Both sorts took the same amount of time.")