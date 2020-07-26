from visualization import Settings
import pygame


def compare_bars(bar1, bar2):
    bar1.color = Settings.GREEN
    bar2.color = Settings.GREEN
    if bar1.height <= bar2.height:
        return True
    return False


def reset_color(bar1, bar2):
    bar1.color = Settings.PINK
    bar2.color = Settings.PINK


def partition(arr, low, high, vis):
    i = (low - 1)         # index of smaller element

    for j in range(low, high):

        bar1 = arr[j]
        bar2 = arr[high]
        # If current element is smaller than or equal to pivot
        if compare_bars(arr[j], arr[high]):

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i].row, arr[j].row = arr[j].row, arr[i].row

        vis.redraw_window()
        vis.update()
        reset_color(bar1, bar2)
        pygame.time.delay(10)
        vis.redraw_window()
        vis.update()
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    arr[i + 1].row, arr[high].row = arr[high].row, arr[i + 1].row

    return (i + 1)


'''
The main function that implements QuickSort

Parameters:
arr (list): Array to be sorted
low (int): Starting Index
high (int): Ending  Index

returns: none
'''
def quickSort(arr, low, high, vis):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high, vis)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1, vis)
        quickSort(arr, pi + 1, high, vis)
