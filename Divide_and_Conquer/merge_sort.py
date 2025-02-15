import random

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

if __name__ == '__main__':
    # Generate a list of 20 random integers between 1 and 100
    random_numbers = [random.randint(1, 100) for _ in range(20)]
    temp = random_numbers
    print(random_numbers)

    merge_sort(random_numbers, 0, len(random_numbers)-1)
    print(random_numbers)

    assert set(random_numbers) == set(temp)
    assert set(random_numbers) == set(sorted(temp))
        