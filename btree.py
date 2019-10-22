# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Edited by Sergio Ortiz
# Last modified October 21, 2019
# Only new methods are commented

import numpy as np
import matplotlib.pyplot as plt

class WordEmbedding(object):
    def __init__(self,word,embedding):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)

class BTree(object):
    # Constructor
    def __init__(self,data,child=[],isLeaf=True,max_data=5):
        self.nodes = 0
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k.word < T.data[i].word:
            return i
    return len(T.data)

#GetEmbedding() - returns the embedding of a specific word
#-->inputs:  T, a btree with many English words
#            k, the word we are searching for
#-->outputs: the embedding of the specified word
def GetEmbedding(T, k):
    N = Search1(T, k)
    if(N is None):
        return None
    for i in range(len(N.data)):
        if N.data[i].word == k:
            return N.data[i].emb
        
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0]) 

#Had to modify to include the embedding
#Insert() - inserts a new word with its embedding to the btree
#by creating a new WordEmbedding object
#-->inputs: T, the btree we want to insert into
#           word, the word we want to insert
#           embedding, the embedding of the word
#-->outputs: None
def Insert(T, word, embedding):
    a = WordEmbedding(word, embedding)
    Insert1(T, a)

#original Insert(), just renamed it    
def Insert1(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i) 
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)  
        
def InsertLeaf(T,i):
    T.data.append(i)
    T.nodes += 1
    Sorter(T.data)
    
def IsFull(T):
    if(T is None):
        return False
    return len(T.data) >= T.max_data

def Leaves(T):
    # Returns the leaves in a b-tree
    if T.isLeaf:
        return [T.data]
    s = []
    for c in T.child:
        s = s + Leaves(c)
    return s

def Print(T):
    # Prints data in tree in ascending order
    if T.isLeaf:
        for t in T.data:
            print(t.word,end=' ')
    else:
        for i in range(len(T.data)):
            Print(T.child[i])
            print(T.data[i].word,end=' ')
        Print(T.child[len(T.data)])
        
def PrintD(T,space):
    # Prints data and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i].word)
    else:
        PrintD(T.child[len(T.data)],space+'   ')  
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i].word)
            PrintD(T.child[i],space+'   ')
            
def Search(T,k):
    #Returns node where k is, or None if k is not in the tree
    if k in T.data.word:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)

#Search1() - searches for a specific word in the bst
#differs from original Search() because that one would search
#for a specific WordEmbedding Object
#-->inputs: T, a btree with many English words and their embeddings
#           k, the word we are looking for
#-->outputs: the node where k is in
def Search1(T, k):
    i = 0
    n = len(T.data) - 1
    while(i < n and k > T.data[i].word):
        i += 1
    if T.data[i].word == k:
        return T
    if T.isLeaf:
        return None
    if(k > T.data[i].word):
        return Search1(T.child[i+1], k)
    return Search1(T.child[i], k)

#Sorter() - used to sort the data in each node
#it is just bubblesort(), I wanted to change it to mergesort() but 
#ran out of time
#-->inputs: T, the b-tree we want to search through
#-->outputs: None
def Sorter(T):
    n = len(T)
    for i in range(n):
        for j in range(0, n-i-1):
            if T[j].word > T[j+1].word :
                T[j], T[j+1] = T[j+1], T[j]
                    
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild,  rightChild   
      







        

  
     
   
    
  
         

 



    




        




    