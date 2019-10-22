# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Edited by Sergio Ortiz
# Last modified October 21, 2019
# Only new methods are commented
import numpy as np

class BST(object):
    # Constructor
    #I added the word, and embedding here, not sure if that is acceptable
    def __init__(self, word, embedding, left=None, right=None):  
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
        self.left = left 
        self.right = right   
        
#GetEmbedding() - returns the embedding of a specific word
#inputs: T, a bst with many English words
#        k, the word we are searching for
#outputs: the embedding of the sepcified word
def GetEmbedding(T, k):
    N = Search(T, k)
    if(N is None):
        return None
    return N.emb

def GetHeight(T):
    if(T is None):
        return 0
    return 1 + GetHeight(T.left)

#GetNumberOfNodes() - returns the number of nodes in the bst
#inputs: T, a bst
#outputs: the number of nodes in the bst, 0 is T is None
def GetNumberOfNodes(T):
    total = 0
    if(T is not None):
        total += Nodes(T)
    return total

def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.word,end=' ')
        InOrder(T.right)

#Had to modify this a bit to include the embedding, 
#but nothing too major
def Insert(T, new_word, embedding):
    if T == None:
        T =  BST(new_word, embedding)
    elif T.word > new_word:
        T.left = Insert(T.left,new_word, embedding)
    else:
        T.right = Insert(T.right,new_word, embedding)
    return T

#Nodes() - counts the nodes in a tree
#inputs: T, a bst
#outputs: the amount of nodes in the bst
def Nodes(T):
    total = 1
    if T.left is not None:
        total += Nodes(T.left)
    if T.right is not None:
        total += Nodes(T.right)
    return total

def Search(T, k):
    if T is None or T.word == k:
        return T
    if T.word < k:
        return Search(T.right, k)
    else:
        return Search(T.left, k)
        
def ShowBST(T,ind):
    # Display rotated BST in text form
    if T is not None:
        ShowBST(T.right,ind+'   ')
        print(ind, T.word)
        print(ind, T.emb)
        ShowBST(T.left,ind+'   ')
        

    








    
   
    