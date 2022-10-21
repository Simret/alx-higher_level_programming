#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find peak"""
    ln = len(list_of_integers)
    if ln == 0:
        return
    half = ln // 2
    if (half == ln - 1 or list_of_integers[half] >=
        list_of_integers[half + 1]) and (half == 0 or list_of_integers[half] >=
                                         list_of_integers[half - 1]):
        return (list_of_integers[half])
    elif half != ln - 1 and list_of_integers[half + 1] > list_of_integers[half]:
        return (find_peak(list_of_integers[half + 1:]))
    return (find_peak(list_of_integers[:half]))
