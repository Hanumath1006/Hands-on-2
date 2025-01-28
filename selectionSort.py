import platform
import random
import time

import matplotlib.pyplot as plt
import psutil


def selection_sort(arr):
    """
    Perform selection sort on the given list.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
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

def benchmark_selection_sort():
    """
    Benchmarks selection sort for different input sizes, plotting time vs. size.
    """
    input_sizes = [5, 10, 20, 100, 200, 500, 1000, 2000, 5000]  # array sizes spanning from 5 to 5000
    avg_times = []

    for size in input_sizes:
        runs = 3  # number of test runs per size
        total_time = 0.0

        for _ in range(runs):
            arr = [random.randint(0, 100000) for _ in range(size)]
            start = time.time()
            selection_sort(arr)
            end = time.time()
            total_time += (end - start)

        avg_time = total_time / runs
        avg_times.append(avg_time)
        print(f"Input size: {size}, Average time: {avg_time:.5f} seconds")

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(input_sizes, avg_times, marker='o', label='Selection Sort')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Selection Sort Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    system_info()
    
    # Example array to demonstrate the sorting algorithm
    example_array = [29, 10, 14, 37, 13]
    print("Example array (unsorted):", example_array)
    sorted_example = selection_sort(example_array.copy())
    print("Example array (sorted):", sorted_example)
    print("\n")
    
    # Benchmark the algorithm
    benchmark_selection_sort()
