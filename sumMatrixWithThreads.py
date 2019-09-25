'''Sum all elements of a matrix using threads'''

import threading

matrix = [[1, 2],[3, 4],[5, 6]]

def run(n, **totalSum):
    for i in range(len(matrix[0])):
        sumThreads['sumThreads'] += matrix[n][i]
    
sumThreads = {"sumThreads":0}
for i in range(len(matrix)):
    t = threading.Thread(target=run, args=(i,), kwargs=(sumThreads))
    t.start() 
print(sumThreads['sumThreads'])
