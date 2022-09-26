# Like a wad of cash data that is structured can be searched, sorted, stored,
# deleted, counted, etc. Data structures are containers of data. Examples include
# arrays, trees, hash tables, indexes, queues, linked lists, stacks, etc. 1-dimensional
# array is info stored in an unbroken block of memory.


# Linear Search
# Like pulling a wad of cash out of your wallet and need a certain big bill; in a linear
# search would have to go through each bill one by one until the target bill was
# located. Use linear search when relatively few #'s and relatively sorted


def search(arr, target):
        for i in range(len(arr)):

            if arr[i] == target:
                return i


my_arr = [2, 5, 8, 9, 10, 16, 22]
our_target = 10

print(search(my_arr, our_target))

# Iterative Binary Search
# "two parts"; create two pointers and repeatedly divide the search  by half.
# Reduces search space by not searching only the divided parts and not the entire
# array. In this kind of search the middle element is evaluated first, and if a
# match returned. If > target, search begins in lower half of array, if < target,
# the upper half.


def binary_itr(arr, start, end, target):

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            return end

    return start
    # return -1


my_arr = [2, 5, 8, 10, 16, 22, 25]
my_target = 10

result = binary_itr(my_arr, 0, len(my_arr) - 1, my_target)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in our array")


def binary_recur(arr, start, end, target):

    if end >= start:

        mid = start + end - 1 // 2

        if arr[mid] < target:
            binary_itr(arr, mid + 1, end, target)

        elif arr[mid] > target:
            return binary_recur(arr, start, mid - 1, target)

        else:
            return mid

    else:
        return -1


my_arr2 = [2, 5, 8, 10, 16, 22, 25]
my_target2 = 10

result = binary_itr(my_arr2, 0, len(my_arr2) - 1, my_target2)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in our array")


# Bubble Sort (outdated)
# Quick sorting algorithm that swaps adjacent elements if they are in the wrong
# order, for example, the largest integer in list of ints. Best use is to see if
# a list is already or nearly sorted, because not very efficient.


def bubble_optimized(a):
    iterations = 0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            iterations += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a, iterations


bub_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_optimized(bub_arr))


# Insertion Sort
# Builds final array one item at a time; sorted/unsorted 'sides'; still inefficient
# on large lists; advantages: doesn't require much space (can be done 'in place'),
# good for small data sets and smaller (relatively sorted) arrays; simple implementation.
# Concept: splits array into two sections--sorted/unsorted; takes one element at a time
# from the unsorted side and compares it to each element on the sorted side. If ele is
# larger or smaller, it places it where it needs to be on the sorted side until there
# are no more ele's to compare it to, leaving a sorted array.

def insertion_sort(a):
    for j in range(1, len(a)):  # for-loop begins at second element in sorted arr (b/c already sorted :) )
        key = a[j]  # current ele
        i = j-1  # pointer to left of key
        while i >= 0 and a[i] > key:  # iterates as long as index is greater or equal to 0 AND greater than key
            a[i + 1] = a[i]  # reassigns the larger ele to the right position
            i -= 1  # move down and put smaller ele to left
        a[i + 1] = key  # reassign key
    return a


a_insert = [5, 2, 4, 6, 1, 3]
print(insertion_sort(a_insert))


