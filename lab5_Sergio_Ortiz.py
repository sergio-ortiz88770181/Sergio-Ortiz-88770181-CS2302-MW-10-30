#CS 2302 Data Structures Fall 2019 MW 10:30
#Sergio Ortiz
#Assignment - Lab #5
#Instructor - Olac Fuentes
#Teaching Assistant - Anindita Nath
#November 1, 2019
#This program will compare the runtimes between 
#a Hash Table with Chaining and a Hash Table with 
#Linear Probing 

import Sergio_Ortiz_HashC as hc
import Sergio_Ortiz_HashLP as hlp
import numpy as np
import time


#buildChaining() - function to build a hash table with chaining
#inputs : None
#outputs: a hash table with a lot of english words        
def buildChaining():
    T = None
    T = hc.HashTableChain(65)
    f = open("glove.6B.50d.txt", encoding = "utf8")
    line = f.readline().split(' ') #creates a list, splits at spaces
    while line[0] != '': #for some reason when I reached the end of the
        #file it would keep creating lists with the empty ['']
        T.insert(line[0], np.asarray(line[1:-1]))
        line = f.readline().split(' ')
    f.close()
    return T

#buildLinear() - builds a hash table with linear probing
#inputs: None
#outputs : a hash table with a lot of English Words
def buildLinear():
    counter = 5000
    T = None
    T = hlp.HashTableLP(99999)
    #f = open("words.txt", encoding = "utf8")
    f = open("glove.6B.50d.txt", encoding = "utf8")
    line = f.readline().split(' ') #creates a list, splits at spaces
    while counter > 0: #line[0] != '': #for some reason when I reached the end of the
        #file it would keep creating lists with the empty ['']
        if ord(line[0][0]) > 64:
            T.insert(line[0], np.asarray(line[1:-1]))
        line = f.readline().split(' ')
        counter -= 1
    f.close()
    return T
    
#chooseTable() - Method for the user to choose which hash table
#inputs: None
#outputs: a number representing either a chaining or linear probing table 
def chooseTable():
    print('(1) Hash Table with Chaining')
    print('(2) Hash Table with Linear Probing')
    choice = int(input('Which Hash Table do you want to use? '))
    return choice

#main() - main method where all the functions go
#No inputs or outputs
def main():
    choice = chooseTable()
    while choice != 1 and choice != 2:
        print()
        print('Please enter 1 or 2')
        choice = chooseTable()
    if choice == 1:
        start = time.time()
        table = buildChaining()
        end = time.time()
        elapsed = end - start
        print('Time to build Hash Table with Chaining: ', elapsed)
        start = time.time()
        SimilaritiesChaining(table)
        end = time.time()
        elapsed = end - start
        print('Time to get similarities: ', elapsed)
    if choice == 2:
        start = time.time()
        table = buildLinear()
        end = time.time()
        elapsed = end - start
        print('Time to build Hash Table with Linear Probing ', elapsed)
        start = time.time()
        SimilaritiesLinear(table)
        end = time.time()
        elapsed = end - start
        print('Time to get similarities: ', elapsed)

def SimilaritiesChaining(T):
    word_file = open("words.txt", "r")
    line = word_file.readline().split(' ')
    while line[0] != '':
        word1 = line[0]
        word2 = line[1].strip('\n')
        a = T.getEmbedding(str(word1))
        b = T.getEmbedding(str(word2))
        numerator = np.dot(a, b)
        den1 = np.linalg.norm(a)
        den2 = np.linalg.norm(b)
        sim = (numerator) / ((den1) * (den2))
        print("Similarity [",str(word1),",",str(word2),"] = ", str(sim))
        line = word_file.readline().split(' ')
        
def SimilaritiesLinear(T):
    word_file = open("words.txt", "r")
    line = word_file.readline().split(' ')
    while line[0] != '':
        word1 = line[0]
        word2 = line[1].strip('\n')
        a = T.getEmbedding(str(word1))
        b = T.getEmbedding(str(word2))
        numerator = np.dot(a, b)
        den1 = np.linalg.norm(a)
        den2 = np.linalg.norm(b)
        sim = (numerator) / ((den1) * (den2))
        print("Similarity [",str(word1),",",str(word2),"] = ", str(sim))
        line = word_file.readline().split(' ')
    
if __name__ == "__main__":
     main()
