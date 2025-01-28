import platform
import random
import time

import matplotlib.pyplot as plt
import psutil


def bubble_sort(arr):
    """
    Perform bubble sort on the given list.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def system_info():
    """
    Prints system information such as OS, CPU, and RAM.
    """
    print("=== System Information ===")
    print("Platform:", platform.system(), platform.release())
    print("Processor:", platform.processor())
    print("CPU count (logical):", psutil.cpu_count(logical=True))
    print("RAM (GB):", round(psutil.virtual_memory().total / (1024**3), 2))
    print("==========================\n")

def benchmark_bubble_sort():
    """
    Benchmarks bubble sort for different input sizes, plotting time vs. size.
    """
    input_sizes = [5, 10, 20, 100, 200, 500, 1000, 2000, 5000]  # Array sizes spanning from 5 to 5000
    avg_times = []

    for size in input_sizes:
        runs = 3  # number of test runs per size
        total_time = 0.0

        for _ in range(runs):
            arr = [random.randint(0, 100000) for _ in range(size)]
            start = time.time()
            bubble_sort(arr)
            end = time.time()
            total_time += (end - start)

        avg_time = total_time / runs
        avg_times.append(avg_time)
        print(f"Input size: {size}, Average time: {avg_time:.5f} seconds")

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(input_sizes, avg_times, marker='o', label='Bubble Sort')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Bubble Sort Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    system_info()
    
    # Example array to demonstrate the sorting algorithm
    example_array = [64, 34, 25, 12, 22, 11, 90]
    print("Example array (unsorted):", example_array)
    sorted_example = bubble_sort(example_array.copy())
    print("Example array (sorted):", sorted_example)
    print("\n")
    
    # Benchmark the algorithm
    benchmark_bubble_sort()

