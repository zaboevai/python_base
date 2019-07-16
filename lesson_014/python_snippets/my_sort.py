# -*- coding: utf-8 -*-


def my_sort_v1(slist):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist) - 1):
            if slist[i] > slist[i + 1]:
                slist[i], slist[i + 1] = slist[i + 1], slist[i]
                was_swap = True
    return slist

def my_sort_v2(slist):
    if len(slist) <= 1:
        return slist
    pivot = slist[0]
    less_then = []
    more_then = []
    for elem in slist:
        if elem > pivot:
            more_then.append(elem)
        elif elem < pivot:
            less_then.append(elem)
    return my_sort(less_then) + [pivot, ] + my_sort(more_then)


def my_sort(slist):
    return list(set(sorted(slist)))
