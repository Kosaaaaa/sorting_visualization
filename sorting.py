def partition(arr, low, high):
    i = (low - 1)         # index of smaller element
    pivot = arr[high].height     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j].height <= pivot:

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


'''
The main function that implements QuickSort

Parameters:
arr (list): Array to be sorted
low (int): Starting Index
high (int): Ending  Index

returns: none
'''
def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
