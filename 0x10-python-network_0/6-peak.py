#!usr/bin/python3
"""
Technical interview preparation
"""


def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers.
    """
    if len(list_of_integers) == 0:
        return None

    L = list_of_integers
    beg = 0
    end = len(L)-1
    mid = (beg+end)//2
    if L[mid-1] < L[mid] and L[mid+1] < L[mid]:
        return L[mid]
    elif L[mid] < L[mid-1]:
        return find_peak(L[beg:mid+1])
    elif L[mid] < L[mid+1]:
        return find_peak(L[mid:end+1])
    else:
        return L[beg]
