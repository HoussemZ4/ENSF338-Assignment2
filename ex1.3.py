from time import perf_counter
from matplotlib import pyplot as plt

def fib_memo(n, memo={}) :
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]

def time_memo(n):
    start = perf_counter()
    result = fib_memo(n)
    stop = perf_counter()
    return stop - start

def fib_old(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_old(n-1) + fib_old(n-2)

def time_old(n):
    start = perf_counter()
    result = fib_old(n)
    stop = perf_counter()
    return stop - start

if __name__ == '__main__':
    old_times = [time_old(n) for n in range(36)] 
    memo_times = [time_memo(n) for n in range(36)]

    fig, axs = plt.subplots(figsize=(9,3))
    axs1 = plt.subplot2grid(shape=(1,2), loc=(0,0))
    axs2 = plt.subplot2grid(shape=(1,2), loc=(0,1))
    plt.suptitle("Time Taken to Compute fib(n) With and Without Memoization")

    axs1.plot(range(36), old_times)
    axs1.set_title("Without Memoization")
    axs1.set_xlabel("Input size (n)")
    axs1.set_ylabel("Time taken (s)")

    axs2.plot(range(36), memo_times)
    axs2.set_title("With Memoization")
    axs2.set_xlabel("Input size (n)")
    axs2.set_ylabel("Time taken (s)")

    plt.show()




