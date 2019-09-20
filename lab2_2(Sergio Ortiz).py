#CS 2302 Data Structures Fall 2019 MW 10:30
#Sergio Ortiz
#Assignment - Lab #2 - Part 2
#Instructor - Olac Fuentes
#Teaching Assistant - Anindita Nath
#September 20, 2019
#This program implements quicksort non - recursively
#as well as select_modified_quick using a while loop

class stackRecord(object):
    def __init__(self, L, start, end):
        self.L = L
        self.start = start
        self.end = end

#partition(): the main function of quicksort
#gets a pivot from a list, and moves everything
#less than it to the left of it and everything
#greater than it to the right
#inputs: L - a list to be sorted
#        start - the start index of the list
#        end - the end index of the list
#output: the index of the pivot
def partition(L, start, end):
    i = (start - 1)
    pivot = L[end]
    for j in range(start, end):
        if(L[j] <= pivot):
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[end] = L[end], L[i+1]
    return(i + 1)

#quick_sort_nr(): a non recursive implementation
#of the naturally recursive algorithm, quicksort
#input: L - the list to be sorted
def quick_sort_nr(L):
    start = 0
    end = len(L) - 1
    quick_sorter_nr(L, start, end)

#quick_sorter_nr(): the actual implementation
#of the non recursive quicksort using a stack
#inputs: L - the list to be sorted
#        start - the start index of the list
#        end - the end index of the list
def quick_sorter_nr(L, start, end):
    stack = [stackRecord(L, start, end)]
    while(len(stack) > 0):
        h = stack.pop(-1)
        if(h.start < h.end):
            part = partition(h.L, h.start, h.end)
            stack.append(stackRecord(h.L, h.start, part - 1))
            stack.append(stackRecord(h.L, part + 1, h.end))

#while_select(): an implementation of the
#select_modified_quick algorithm without using recursion
#or stacks
#inputs: L - the list to be traversed
#        k - the index of the desired element
#outputs: the value of L[k]
def while_select(L,k):
    start = 0
    end = len(L) - 1
    return while_selector(L, start, end, k)

#while_selector(): the algorithm for select_modified_quick
#using a while loop
#inputs: L - the list to be traversed
#        start - the beginning index
#        end - the end index
#        k - the index of the element we are looking for
#outputs: the value of L[k]
def while_selector(L, start, end, k):
    pivot = partition(L, start, end)
    while(pivot != k):
        if(k < pivot):
            pivot = partition(L, start, pivot -1)
        elif(k > pivot):
            pivot = partition(L, pivot + 1, end)
    return L[pivot]


if __name__ == "__main__":
    L1 = [6,3,7,3,1,7,8,9,6,4,1,6]
    quick_sort_nr(L1)
    print(L1)
    L = [4,2,7,3,2]
    print(while_select(L, 0))

