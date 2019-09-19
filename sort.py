import sys, time, random, visualizer

vis = visualizer.Visualizer(600, 600)

def main():

  gen_list = [i for i in range(100)]
  random.shuffle(gen_list)

  args = [arg.lower() for arg in sys.argv[1:]]
  if 'bubble' in args:
    start_time = time.perf_counter_ns()
    bubble_sort(gen_list[:])
    end_time = time.perf_counter_ns()

    vis.replay(0)
    vis.reset()

    print('Bubble Sort')
    print(f'Time: {end_time - start_time:,}ns\n')

  elif 'insertion' in args:
    start_time = time.perf_counter_ns()
    insertion_sort(gen_list[:])
    end_time = time.perf_counter_ns()

    vis.replay(0)
    vis.reset()

    print('Insertion Sort')
    print(f'Time: {end_time - start_time:,}ns\n')

  elif 'selection' in args:
    start_time = time.perf_counter_ns()
    selection_sort(gen_list[:])
    end_time = time.perf_counter_ns()

    vis.replay(0)
    vis.reset()

    print('Selection Sort')
    print(f'Time: {end_time - start_time:,}ns\n')
  elif 'merge' in args:
    pass
  elif 'heap' in args:
    start_time = time.perf_counter_ns()
    heap_sort(gen_list[:])
    end_time = time.perf_counter_ns()

    vis.replay(0)
    vis.reset()

    print('Heap Sort')
    print(f'Time: {end_time - start_time:,}ns\n')
  elif 'shell' in args:
    gaps = [10, 5, 3, 2, 1]

    start_time = time.perf_counter_ns()
    shell_sort(gen_list[:], gaps)
    end_time = time.perf_counter_ns()

    vis.replay(0)
    vis.reset()

    print('Shell Sort')
    print(f'Time: {end_time - start_time:,}ns\n')
  elif 'comb' in args:
    start_time = time.perf_counter_ns()
    comb_sort(gen_list[:], 1.3)
    end_time = time.perf_counter_ns()

    vis.replay(0)
    vis.reset()

    print('Comb Sort')
    print(f'Time: {end_time - start_time:,}ns\n')
  elif 'cocktail' in args:
    start_time = time.perf_counter_ns()
    cocktail_shaker_sort(gen_list[:])
    end_time = time.perf_counter_ns()

    vis.replay(0)
    vis.reset()

    print('Cocktail Shaker Sort')
    print(f'Time: {end_time - start_time:,}ns\n')
  elif 'quick' in args:
    start_time = time.perf_counter_ns()
    quick_sort(gen_list[:], 0, len(gen_list) - 1)
    end_time = time.perf_counter_ns()

    vis.replay(0)
    vis.reset()

    print('Quick Sort')
    print(f'Time: {end_time - start_time:,}ns\n')

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

      vis.update(lst[:], [i, i + 1])

      if lst[i + 1] < lst[i]:
        lst[i + 1], lst[i] = lst[i], lst[i + 1]
        sorted = False
    if sorted:
      return lst
    length -= 1

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
    vis.update(lst[:], [i])
    while j > 0 and lst[j - 1] > lst[j]:
      vis.update(lst[:], [j, j - 1])
      lst[j], lst[j - 1] = lst[j - 1], lst[j]
      j = j - 1
  vis.update(lst[:])
  return lst

# Selection Sort
#
# Iterates through each element in a list, swapping it's value with the
# smallest value ahead of it.
#
# Data structure: Array
#
# Time complexity:
#   Worst:    O(n^2) comparisons,
#             O(n) swaps
#   Best:     O(n^2) comparisons,
#             O(n) swaps
#   Average:  O(n^2) comparisons,
#             O(n) swaps
#
# Worst-case space complexity:
#   Auxillary:  O(1)
def selection_sort(lst):
  for i in range(len(lst)):
    min_item = min(lst[i:])
    vis.update(lst[:], [i, lst.index(min_item)])
    lst[lst.index(min_item)], lst[i] = lst[i], lst[lst.index(min_item)]
  vis.update(lst[:])
  return lst

# Merge Sort
#
# Divides the unsorted list into sublists, each containing one element.
# Repeatedly merges the sublists into new sorted lists until only one sublist
# remains.
#
# Data structure: Array
#
# Time complexity:
#   Worst:    O(n log n)
#   Best:     O(n log n) typical,
#             O(n) natural variant
#   Average:  O(n log n)
#
# Worst-case space complexity:
#   Total:      O(n)
#   Auxillary:  O(n),
#               O(1) with linked-lists
def merge_sort(lst):
  if len(lst) <= 1:
    return lst
  middle = int(len(lst) / 2)
  left = merge_sort(lst[:middle])
  right = merge_sort(lst[middle:])

  return merge(left, right)

def merge(left, right):
  result = []
  while len(left) is not 0 and len(right) is not 0:
    if left[0] < right[0]:
      result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]
  for i in left:
    result.append(i)
  for i in right:
    result.append(i)
  return result

# start_time = time.perf_counter_ns()
# sorted = merge_sort(gen_list[:])
# end_time = time.perf_counter_ns()

# print('Merge Sort')
# print(f'Time: {end_time - start_time:,}ns')
# print()

# Heap Sort
#
# Prepares the list by turning it into a max heap. Repeatedly swaps the first
# value in the heap with the last value, decreasing the range of values
# considered in the heap operation by one, and sifting the new first value into
# its position in the heap.
#
# Data structure: Array
#
# Time complexity:
#   Worst:    O(n log n)
#   Best:     O(n log n) distinct keys,
#             O(n) equal keys
#   Average:  O(n log n)
#
# Worst-case space complexity:
#   Total:      O(n)
#   Auxillary:  O(1)
def heap_sort(lst):
  heapify(lst)
  end = len(lst) - 1
  while end > 0:
    lst[end], lst[0] = lst[0], lst[end]
    end -= 1
    sift_down(lst, 0, end)
  return lst

def heapify(lst):
  start = int(((len(lst) - 1) - 1) / 2)
  while start >= 0:
    sift_down(lst, start, len(lst) - 1)
    start -= 1

def sift_down(lst, start, end):
  while start * 2 + 1 <= end:
    child = start * 2 + 1
    vis.update(lst[:], [start, child])
    swap = start
    if lst[child] > lst[swap]:
      swap = child
    if lst[child - 1] > lst[swap]:
      swap = child - 1
    if swap is start:
      return
    else:
      lst[start], lst[swap] = lst[swap], lst[start]
      start = swap
  vis.update(lst[:])

# Shell Sort
#
# Data structure: Array
#
# Time complexity:
#   Worst:    O(n^2) worst known worst case gap sequence,
#             O(n log n^2) best known worst case gap sequence
#   Best:     O(n log n) most gap sequences,
#             O(n log n^2) best known worst case gap sequence
#   Average:  depends on the sequence
#
# Worst-case space complexity:
#   Total:      O(n)
#   Auxillary:  O(1)
def shell_sort(lst, gaps):
  length = len(lst)
  for gap in gaps:
    for i in range(length - gap):
      j = i + gap
      while j >= gap and lst[j - gap] > lst[j]:
        vis.update(lst[:], [j, j - gap])
        lst[j], lst[j - gap] = lst[j - gap], lst[j]
        j -= gap
  vis.update(lst[:])
  return lst

# Comb Sort
#
# Data structure: Array
#
# Time complexity:
#   Worst:    O(n^2)
#   Best:
#   Average:
#
# Worst-case space complexity:
#   Total: O(1)
def comb_sort(lst, shrink):
  length = len(lst)
  gap = length
  sorted = False

  while not sorted:
    gap = int(gap / shrink)
    if gap <= 1:
      gap = 1
      sorted = True
    i = 0
    while i < length - gap:
      vis.update(lst[:], [i, i + gap])
      if lst[i + gap] < lst[i]:
        lst[i + gap], lst[i] = lst[i], lst[i + gap]
        sorted = False
      i += 1
    vis.update(lst[:])
  return lst

# Cocktail Shaker Sort
#
# Data structure: Array
#
# Time complexity:
#   Worst:    O(n^2)
#   Best:     O(n)
#   Average:  O(n^2)
#
# Worst-case space complexity:
#   Total: O(1)
def cocktail_shaker_sort(lst):
  start = 0
  end = len(lst)
  while 1:
    sorted = True
    for i in range(start, end - 1):
      if lst[i + 1] < lst[i]:
        lst[i + 1], lst[i] = lst[i], lst[i + 1]
        sorted = False
      vis.update(lst[:], [i, i + 1])
    end -= 1
    if sorted:
      return lst
    for i in range(end - 1, start, -1):
      if lst[i - 1] > lst[i]:
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
        sorted = False
      vis.update(lst[:], [i, i - 1])
    start += 1
    if sorted:
      return lst

# start_time = time.perf_counter_ns()
# sorted = cocktail_shaker_sort(gen_list[:])
# end_time = time.perf_counter_ns()

# print('Cocktail Shaker Sort')
# print(f'Time: {end_time - start_time:,}ns')
# print()

# Quick Sort
#
# Data structure:
#
# Time complexity:
#   Worst:    O(n^2)
#   Best:     O(n log n) simple partition
#             O(n) three-way partition and equal keys
#   Average:  O(n log n)
#
# Worst-case space complexity:
#   Auxillary (naive):  O(n)
#   Auxillary:          O(log n)
def quick_sort(lst, lo, hi):
  if lo < hi:
    p = partition(lst, lo, hi)
    quick_sort(lst, lo, p)
    quick_sort(lst, p + 1, hi)
  vis.update(lst[:])
  return lst

def partition(lst, lo, hi):
  pivot = lst[int(lo + (hi - lo) / 2)]
  while 1:
    while lst[lo] < pivot:
      lo += 1
      vis.update(lst[:], [lo, pivot, hi])
    while lst[hi] > pivot:
      hi -= 1
      vis.update(lst[:], [lo, pivot, hi])
    if lo >= hi:
      return hi
    lst[lo], lst[hi] = lst[hi], lst[lo]
    lo += 1
    hi -= 1

if __name__ == '__main__':
  main()