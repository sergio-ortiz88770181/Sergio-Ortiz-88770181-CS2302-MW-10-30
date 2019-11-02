# Implementation of hash tables with linear probing
# Programmed by Olac Fuentes
#Edited by Sergio Ortiz
# Last modified November 1, 2019

import numpy as np
from numpy import array as narray

class WordEmbedding(object):
    def __init__(self,word,embedding):
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32)

class HashTableLP(object):
    # Builds a hash table of size 'size', initilizes items to -1 (which means empty)
    # Constructor
    def __init__(self,size):  
         self.item = narray(-1, dtype = object)
         for i in range(size - 1):
             self.item = np.insert(self.item, 1, -1)
    #returns the embedding of a specific word
    #inputs: k - the word we are searching for
    #outputs: the embedding of the given word    
    def getEmbedding(self, k):
        position = self.h4(k)
        #position = self.h5(k)
        if self.item[position] == -1 or self.item[position] == -2:
            return -1
        while self.item[position].word != k:
            position += 1
            if self.item[position] == -1 or self.item[position] == -2:
                return -1
        return self.item[position].emb    
    
    #the first hashing method, takes the length of the word
    #and modulo by the length of the hash table
    def h1(self, k):
        return (len(k)) % len(self.item)
    
    #the second hashing method, takes the ASCII values of 
    #the first letter and modulo by length of hash table
    def h2(self,k):
        return k % len(self.item)  
    
    #the third hashing method, takes product of first
    #and last ASCII values and modulo it
    def h3(self, k):
        product = ord(k[0]) * ord(k[-1])
        return product % len(self.item)
    
    #the fourth hashing method, takes the sum of the ASCII
    #values and modulo it
    def h4(self, k):
        sum = 0
        for i in range(len(k)):
            sum += ord(k[i])
        return sum % len(self.item)
    
    #the fifth hashing method, uses recurssion
    #I could not get this one to work
    def h5(self, k):
        return self.h5_1(k, len(self.item))
    
    def h5_1(self, s, n):
        return (ord(s[0]) + 255 * self.h5_1(s[1:],n)) % n
    
    #hashing method of my choice, takes the sum of the ASCII
    #values and divided it by two, then modulo it
    def h6(self, k):
        sum = 0
        for i in range(len(k)):
            sum += ord(k[i])
        return (sum // 2) % len(self.bucket)
    
    #insert() - inserts a word embedding object into the 
    #hash table
    #inputs: word - the word we want to input
    #        embedding - the embedding of the word
    #outputs: None
    def insert(self, word, embedding):
        new_word = WordEmbedding(word, embedding)
        self.insert1(new_word)
    
    def insert1(self, k):
        bucket = self.h4(k.word)
        #bucket = self.h5(k)
        bucketsProbed = 0
        while bucketsProbed < len(self.item):
            if self.item[bucket] == -1 or self.item[bucket] == -2:
                self.item[bucket] = k
                return bucket
            bucket = (bucket + 1) % len(self.item)
            bucketsProbed += 1
        return -1
    
    #print_contents() - prints the words in the hash table
    #shows the actual words instead of a WordEmbedding 
    #object
    def print_contents(self):
        print('Table contents:')
        for i in range(len(self.item)):
            if self.item[i] != -1 and self.item[i] != -2:
                print(self.item[i].word)
            else:
                print(self.item[i])
    
    #print_table() - prints the table
    #only downside is that it shows all the contents as 
    #a WordEmbedding object         
    def print_table(self):
        print('Table contents:')
        print(self.item)
        
    
                
    
            
            
    