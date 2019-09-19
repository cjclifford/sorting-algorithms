import time, random

gen_list = [i for i in range(2000)]
random.shuffle(gen_list)

# Bubble Sort
#
# Repeatedly iterates through each element in a list, compares adjacent elements
# and swaps them if they're in the wrong order, decreasing the considered range
# by 1 for each run that swaps values, until a run where no swaps occurs.
#
# Data structure: Array
#
# Time complexity:
#   Worst:    O(n^2) comparisons and swaps
#   Best:     O(n) comparisons,
#             O(1) swaps
#   Average:  O(n^2) comparisons and swaps
#
# Worst-case space complexity:
#   Auxillary: O(1)
def bubble_sort(lst):
  length = len(lst) - 1
  while 1:
    sorted = True
    for i in range(length):
      if lst[i + 1] < lst[i]:
        lst[i + 1], lst[i] = lst[i], lst[i + 1]
        sorted = False
    if sorted:
      return lst
    length -= 1

start_time = time.perf_counter_ns()
sorted = bubble_sort(gen_list[:])
end_time = time.perf_counter_ns()

print('Bubble Sort')
print(f'Time: {end_time - start_time:,}ns')
print()

# Insertion Sort
#
# Iterates through each element in a list, continuously swapping with it's
# previous value if current value is smaller than the prior.
#
# Data structure: Array
#
# Time complexity:
#   Worst:    O(n^2) comparisons and swaps
#   Best:     O(n) comparisons and swaps
#   Average:  O(n^2) comparisons and swaps
#
# Worst-case space complexity:
#   Total:      O(n)
#   Auxillary:  O(1)
def insertion_sort(lst):
  for i in range(len(lst)):
    j = i
    while j > 0 and lst[j - 1] > lst[j]:
      lst[j], lst[j - 1] = lst[j - 1], lst[j]
      j = j - 1
  return lst

start_time = time.perf_counter_ns()
sorted = insertion_sort(gen_list[:])
end_time = time.perf_counter_ns()

print('Insertion Sort')
print(f'Time: {end_time - start_time:,}ns')
print()