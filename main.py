from heap_sort import heap_sort

# unsorted
li = [1, 4, 8, 23, 6, 9, 3, 5]
print(f"Sort results on unsorted list {heap_sort(li)}")

# sorted
li = [1, 3, 4, 5, 6, 8, 9, 23]
print(f"Sort results on sorted list {heap_sort(li)}")

# reversed
li = [23, 9, 8, 6, 5, 4, 3, 1]
print(f"Sort results on reversed list {heap_sort(li)}")

# same
li = [23, 23, 23, 23, 23, 23, 23, 23]
print(f"Sort results on same items list {heap_sort(li)}")
