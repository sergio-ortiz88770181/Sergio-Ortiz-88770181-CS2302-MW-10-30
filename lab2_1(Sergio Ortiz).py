#CS 2302 Data Structures Fall 2019 MW 10:30
#Sergio Ortiz
#Assignment - Lab #2 - Part 1
#Instructor - Olac Fuentes
#Teaching Assistant - Anindita Nath
#September 20, 2019
#This program implements select_bubble(L,k), select_quick(L, k)
#and select_modified_quick(L, k)

#bubble_sort(): will sort a given list using
#the bubble sort algorithm
#input: L - the list to be sorted
#output: list L sorted in acending order
def bubble_sort(L):
    for i in range(len(L)):
        for j in range((len(L) - 1) - i):
            if(L[j] >= L[j+1]):
                L[j], L[j+1] = L[j+1], L[j]
    return L

#partition(): the main part of the quicksort algorithm,
#this method will find a pivot and place it in its correct
#place by moving everything smaller than it to its right and
#eveything bigger to its right
#inputs: L - the list to be sorted
#        start - the start index
#        end - the end index
# output: the index of the pivot
def partition(L, start, end):
    i = (start - 1)
    pivot = L[end]
    for j in range(start, end):
        if(L[j] <= pivot):
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[end] = L[end], L[i+1]
    return(i + 1)

#select_bubble(): will select the kth smallest
#value of a given list
#inputs: L - the list to be traversed
#        k - the position we are looking for
#outputs: the value of L[k]
def select_bubble(L,k):
    bubble_sort(L)
    return L[k]

#select_modified_quick(): will find the kth
#smallest value of a list using a modified
#version of quicksort
#inputs: L - the list to be traversed
#        k - the position we are looking for
#output: the value at L[k]
def select_modified_quick(L, k):
    start = 0
    end = len(L) - 1
    return selector(L, start, end, k)

#select_quick(): will select the kth smallest
#element in the list using quicksort
#inputs: L - the list to be sorted and traversed
#        k - the position we are looking for
#output: the value of L[k]
def select_quick(L,k):
    quick_sort(L)
    return L[k]

#selector(): the quickselect algorithm
#inputs: L - the list to be traversed
#        start - the beginning index
#        end - the end index
#        k - the index we are searching for
#ouput: the value of L[k]
def selector(L, start, end, k):
    pivot = partition(L, start, end)
    if(k < pivot):
        return selector(L, start, pivot - 1, k)
    elif(k == pivot):
        return L[pivot]
    else:
        return selector(L, pivot + 1, end, k)

#sortq(): the sorting algorithm for quicksort
#inputs: L - the array to be sorted
#        start - the start index
#        end - the end index
def sortq(L, start, end):
    if(start < end):
        part = partition(L, start, end)
        sortq(L, start, part - 1)
        sortq(L, part + 1, end)

#quick_sort(): the quicksort algorithm
#inputs: L - the list to be sorted
def quick_sort(L):
    start = 0
    end = len(L) - 1
    sortq(L, start, end)

