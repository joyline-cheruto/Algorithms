def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []
    for item in sequence:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)
    return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)
print(quick_sort([2,9,7,1,0,5]))