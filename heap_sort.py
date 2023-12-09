# sort heap
def down_heap(li, k, n):
    swaps_ = 0
    comparisons_ = 0
    new_elem = li[k]
    while k <= n / 2:
        comparisons_ += 1
        child = 2 * k
        if child < n and li[child] < li[child + 1]:
            child += 1
        if new_elem >= li[child]:
            break

        swaps_ += 1
        li[k] = li[child]
        k = child

    swaps_ += 1
    li[k] = new_elem
    return swaps_, comparisons_

def heap_sort(list_):
    swaps_total = 0
    comparisons_total = 0

    size = len(list_)
    # prepare initial heap
    for i in range(round(size / 2 - 1), -1, -1):
        swaps_, comparisons_ = down_heap(list_, i, size - 1)
        swaps_total += swaps_
        comparisons_total += comparisons_

    # sort heap iterations
    for i in range(size - 1, 0, -1):
        temp = list_[i]
        list_[i] = list_[0]
        list_[0] = temp
        swaps_total += 1

        swaps_, comparisons_ = down_heap(list_, 0, i - 1)
        swaps_total += swaps_
        comparisons_total += comparisons_

    print(f"\nPerformed swaps in total: {swaps_total}; Performed comparisons:"
          f" {comparisons_total}")
    return list_
