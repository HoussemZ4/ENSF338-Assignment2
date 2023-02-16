import json
import sys
from time import perf_counter
from matplotlib import pyplot as plt
import random

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1 
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def time_funct1(arr, low, high):
    start = perf_counter()
    func1(arr, low, high)
    stop = perf_counter()
    return stop - start

if __name__ == '__main__':
    with open("ex2.json", "r") as file_read:
        data = json.load(file_read)
    
    for i in range(len(data)):
        random.shuffle(data[i])
    
    sys.setrecursionlimit(20000)

    times = [time_funct1(data[i], 0, len(data[i]) - 1) for i in range(len(data))]
    lengths = [len(data[i]) for i in range(len(data))]
    plt.scatter(lengths, times)
    plt.xlabel("Length of Array")
    plt.ylabel("Time (s)")
    plt.title("Time vs Length of Array to be Sorted")
    plt.show()

