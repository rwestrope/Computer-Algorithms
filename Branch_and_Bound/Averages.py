LCdata = []
with open(r'LCOutputs.txt') as f:
    for line in f:
        fields = line.split()
        rowdata = map(float, fields)
        LCdata.extend(rowdata)

LC_average =sum(LCdata)/len(LCdata)
print("Average time for Least Cost Algorithm:", LC_average)

FIFOdata = []
with open(r'FIFOOutputs.txt') as f:
    for line in f:
        fields = line.split()
        rowdata = map(float, fields)
        FIFOdata.extend(rowdata)

FIFO_average = sum(FIFOdata)/len(FIFOdata)
print("Average time for Breadth First Algorithm:", FIFO_average)

if FIFO_average > LC_average:
    print('Least Cost algorithm was faster.')
else:
    print('Breadth First algorithm was faster.')