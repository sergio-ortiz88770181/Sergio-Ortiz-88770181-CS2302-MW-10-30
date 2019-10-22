#CS 2302 Data Structures Fall 2019 MW 10:30
#Sergio Ortiz
#Assignment - Lab #4
#Instructor - Olac Fuentes
#Teaching Assistant - Anindita Nath
#October 21, 2019
#This program will compare the runtimes between 
#binary search trees and B-trees
import bst #import the binary search tree implementation
import btree #import the btree implementation
import numpy as np
import time

#BuildBST() - builds the binary search tree
#-->input: None
#-->output: an implemented bst with all the words in the file
def BuildBST():
    T = None
    #I dont know what 'encoding' is but I was getting an error and that
    #fixed it
    f = open("glove.6B.50d.txt", encoding = "utf8")
    line = f.readline().split(' ') #creates a list, splits at spaces
    while line[0] != '': #for some reason when I reached the end of the
        #file it would keep creating lists with the empty ['']
        T = bst.Insert(T, line[0], np.asarray(line[1:-1]))
        line = f.readline().split(' ')
    f.close()
    return T

#BuildBTree() - builds the B-tree
#-->input: max_node, the maximum data in a node
#-->output: an implemented B-Tree with all the words in the file
def BuildBTree(max_node):
    T = None
    T = btree.BTree([],max_data=max_node)
    f = open("glove.6B.50d.txt", encoding = "utf8" )
    line = f.readline().split(' ')
    while line[0] != '':
        btree.Insert(T, line[0], np.asarray(line[1:-1]))
        line = f.readline().split(' ')
    f.close()
    return T

#chooseTable() - method which prompts the user to choose
#a table implementation
#-->inputs: None
#-->outputs: an int representing either a bst or a btree
def chooseTable():
    print("Choose table implementation")
    return int(input("Type 1 for binary search tree or 2 B-Tree "))

#main() - main method where everything happens
#-->inputs: None
#-->outputs: None
def main():
    t = chooseTable() #to hold user's choice of table
    T = None #the actual table
    while t != 1 and t != 2:
        print("Please enter 1 or 2")
        t = chooseTable()
    
    if t == 1:
        print("Choice: ", t)
        print()
        print("Building binary search tree")
        print()
        start = time.time()
        T = BuildBST()
        end = time.time()
        elapsed = end - start
        print("Binary Search Tree Stats:")
        print("Number of Nodes: ", bst.GetNumberOfNodes(T))
        print("Height: ", bst.GetHeight(T))
        print("Running time for binary search tree construction: ", elapsed," seconds")
        print()
        print("Reading word file to determine similarities")
        print()
        print("Word Similarities found: ")
        start = time.time()
        SimilaritiesBST(T)
        end = time.time()
        elapsed = end - start
        print()
        print("Running time for binary search tree query processing: ", elapsed," seconds")
    else:
        print("Choice: ", t)
        max_node = int(input("What is the maximum number of items"
                             " you want to store in a node? "))
        print()
        print("Building B - tree")
        print()
        start = time.time()
        T = BuildBTree(max_node)
        end = time.time()
        elapsed = end - start
        print("B - tree stats:")
        print("Number of Nodes: ", T.nodes)
        print("Height: ", btree.Height(T))
        print("Running time for B-tree construction (with max_items = ",max_node,"):", elapsed," seconds")
        print()
        print("Reading word file to determine similarities")
        print()
        print("Word Similarities found: ")
        start = time.time()
        SimilaritiesBTree(T)
        end = time.time()
        elapsed = end - start
        print("Running time for binary search tree query processing: ", elapsed," seconds")
        
#SimilaritiesBST() - checks the similarities in a file using bst
#-->inputs: T, a bst containing a lot of english words and their embeddings
#-->outputs: None
def SimilaritiesBST(T):
    word_file = open("words.txt", "r")
    line = word_file.readline().split(' ')
    while line[0] != '':
        word1 = line[0]
        word2 = line[1].strip('\n')
        a = bst.GetEmbedding(T, str(word1))
        b = bst.GetEmbedding(T, str(word2))
        numerator = np.dot(a, b)
        den1 = np.linalg.norm(a)
        den2 = np.linalg.norm(b)
        sim = (numerator) / ((den1) * (den2))
        print("Similarity [",str(word1),",",str(word2),"] = ", str(sim))
        line = word_file.readline().split(' ')

#SimilaritiesBTree() - checks the similarities in a file using B - Tree
#-->inputs: T, a B-Tree containing a lot of english words and their embeddings 
#-->outputs: None        
def SimilaritiesBTree(T):
    print("Reading word file to determine similarities")
    word_file = open("words.txt", "r")
    line = word_file.readline().split(' ')
    while line[0] != '':
        word1 = line[0]
        word2 = line[1].strip('\n')
        a = btree.GetEmbedding(T, str(word1))
        b = btree.GetEmbedding(T, str(word2))
        numerator = np.dot(a, b)
        den1 = np.linalg.norm(a)
        den2 = np.linalg.norm(b)
        sim = (numerator) / ((den1) * (den2))
        print("Similarity [",str(word1),",",str(word2),"] = ", str(sim))
        line = word_file.readline().split(' ')

if __name__ == "__main__":
     main()