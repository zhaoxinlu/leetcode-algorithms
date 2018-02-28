# -*- coding: utf-8 -*-
def partition(arr, left, right):
    low = left
    high = right
    key = arr[low]

    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        arr[low] = arr[high]

        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]

        arr[low] = key

    return low

def QuickSort(arr, left, right):
    if left < right:
        low = partition(arr, left, right)
        QuickSort(arr, left, low-1)
        QuickSort(arr, low+1, right)

    return arr

if __name__ == '__main__':
    arr = [6, 8, 1, 4, 3, 9]
    print QuickSort(arr, 0, len(arr)-1)