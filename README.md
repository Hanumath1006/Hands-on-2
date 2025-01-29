# Hands-on-2 

Question 2 - Argue Selection Sort Correctness

The array is sorting unsorted arrays and returning sorted arrays. Invariant - at the beginning of the i-th iteration, the first i elements of the array contain the smallest i elements in sorted order. Base case - before the first iteration (i = 0), the first i elements (i.e, an empty set) are trivially sorted. Since there are no elements to compare yet, our invariant is true initially. Assume that at the start of iteration i, the first i elements are sorted. The algorithm selects the smallest element from the remaining unsorted elements. This element is swapped with the first unsorted element at index i, ensuring that the first i + 1 elements remain sorted. We maintain the invariant since we always place the smallest remaining element at index i. At the last iteration, (i = n -1, the loop invariant tells us that the first n -1 elements are correctly sorted. Since the last element is the only remaining unsorted element, and it must be the largest, it is already in the correct position. Thus, the tnire array is sorted when the algorithm terminates. The algorithm does what it is intended to do. 

Question 3 - Benchmark the runtime of each algorithm

The benchmarks of each algorithm should be displayed once each of the python file in this repository is run. Run the files through the command line in this format "python filename.py". Once each file is run, the output display the times the algorithm takes for varying input sizes from 5 to 5000. A graph of size vs time for each algorithm is also displayed. Each array is run 3 times to get the benchmark readings. Below is the system information in which the algorithms were benchmarked on. 

System Information 

Platform: Windows 10

Processor: Intel64 Family 6 Model 140 Stepping 1, GenuineIntel

CPU count(logical): 8

RAM(GB): 15.74

Here are the outputs when run on this machine 

# Insertion Sort
![image](https://github.com/user-attachments/assets/d6fe579c-2de0-4955-b6e8-431520474346)
![image](https://github.com/user-attachments/assets/7959d4b8-be0a-4726-9193-a1b76472924c)

# Selection Sort
![image](https://github.com/user-attachments/assets/458444db-1828-4d9b-ac95-9cb9160a822a)
![image](https://github.com/user-attachments/assets/f5f76efa-4b9b-4f5a-be0d-f36b2056180c)

# Bubble Sort
![image](https://github.com/user-attachments/assets/3c8fa971-b6f9-4ec9-bb1c-33ab1d60c7a0)
![image](https://github.com/user-attachments/assets/5b7234b3-8d4f-4563-9c24-81542e951786)









