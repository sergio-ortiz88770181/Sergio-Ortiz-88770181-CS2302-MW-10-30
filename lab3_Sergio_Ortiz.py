import math

#Node object: used to hold the data
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#List class: has references between nodes,
#creating a list
class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

#Clear(): removes the list of all its elements
    def Clear(self):
        self.head = None

#Delete(): deletes a specific number
#input i: the specific value we want to delete
    def Delete(self, i):
        while(self.head.data == i):
            if(self.head.next is None):
                self.head = None
                return
            self.head = self.head.next
        t = self.head
        j = t
        k = self.tail
        while(t.next is not None):
            if(t.next.data == i):
                t.next = t.next.next
            else:
             t = t.next
        k = t
        self.head = j
        self.tail = k

#HasDuplicates(): Checks if the list has duplicates
    def HasDuplicates(self):
        if(self.head is None):
            return False
        t = self.head
        while(t.next is not None):
            if(t.data == t.next.data):
                return True
            t = t.next
        return False

#IndexOf(): returns the index of a specific number
#input i: the number whose index we are searching for
    def IndexOf(self, i):
        counter = 0
        t = self.head
        while(t.data != i):
            counter += 1
            t = t.next
            if(t is None):
                return -1
        return counter

#Insert(): The main meat of the Sorted List, inserts
#new data to list
#input x: the number we want to insert
    def Insert(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            if(x >= self.tail.data):
                self.tail.next = Node(x)
                self.tail = self.tail.next
            elif(x <= self.head.data):
                i = self.head
                t = Node(x)
                t.next = i
                self.head = t
            else:
                t = self.head
                i = t
                while(t is not None and t.next.data < x):
                    t = t.next
                insertion = Node(x)
                insertion.next = t.next
                t.next = insertion
                self.head = i

#Max(): returns the max elemenet
#output: the max element
    def Max(self):
        if(self.head is None):
            return math.inf
        return self.tail.data

    def Merge(self, M):
        t = self.head
        i = M.head
        new_list = List()
        while(t is not None):
            new_list.Insert(t.data)
            t = t.next
        while(i is not None):
            new_list.Insert(i.data)
            i = i.next
        self.head = new_list.head

#Min(): returns the minimum element
#output: the minimum element
    def Min(self):
        if(self.head is None):
            return math.inf
        return self.head.data

#Print(): prints the contents of the list
#output: the contents of the list
    def Print(self):
        t = self.head
        while t is not None:
            print(t.data, end=' ')
            t = t.next
        print()

#Select(): selects the kth smallest element
#Input k: the index we are searching for
#Output: the value of the list at k
    def Select(self, k):
        if(self.head is None):
            return math.inf
        t = self.head
        while(t is not None  and k > 0):
            t = t.next
            k -= 1
        if(t is None):
            return math.inf
        return t.data

