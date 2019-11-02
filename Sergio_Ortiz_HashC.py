# Implementation of hash tables with chaining
# Programmed by Olac Fuentes
#Edited by Sergio Ortiz
# Last modified November 1, 2019
import numpy as np

class WordEmbedding(object):
    def __init__(self,word,embedding):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)

class HashTableChain(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.bucket = [[] for i in range(size)]
      
    #returns the embedding of a specific word
    #inputs: word_1 - the word we are searching for
    #outputs: the embedding of the given word
    def getEmbedding(self, word_1):
        #position = self.h2(word_1)
        position = self.h4(word_1)
        for i in range(len(self.bucket[position])):
            if self.bucket[position][i].word == word_1:
                return self.bucket[position][i].emb
        return -1    
        
    #the first hashing method, takes the length of the word
    #and modulo by the length of the hash table
    def h1(self, k):
        return (len(k)) % len(self.bucket)
        
    #the second hashing method, takes the ASCII values of 
    #the first letter and modulo by length of hash table
    def h2(self,k):
        return ord(k[0]) % len(self.bucket)   
    
    #the third hashing method, takes product of first
    #and last ASCII values and modulo it
    def h3(self, k):
        product = ord(k[0]) * ord(k[-1])
        return product % len(self.bucket)
    
    #the fourth hashing method, takes the sum of the ASCII
    #values and modulo it
    def h4(self, k):
        sum = 0
        for i in range(len(k)):
            sum += ord(k[i])
        return sum % len(self.bucket)
    
    #the fifth hashing method, uses recurssion
    #I could not get this one to work
    def h5(self, k):
        return self.h5_1(k, len(self.bucket))
    
    def h5_1(self, s, n):
        return (ord(s[0]) + 255 * self.h5_1(s[1:],n)) % n
    
    #hashing method of my choice, takes the sum of the ASCII
    #values and divided it by two, then modulo it
    def h6(self, k):
        sum = 0
        for i in range(len(k)):
            sum += ord(k[i])
        return (sum // 2) % len(self.bucket)
    
    #inOrderPrint() - prints all the values of the hash
    #table in order
    def inOrderPrint(self):
        print('Words:')
        for b in self.bucket:
            for i in range(len(b)):
                print(b[i].word)    
    
    #insert() - inserts a word embedding object into the 
    #hash table
    #inputs: word - the word we want to input
    #        embedding - the embedding of the word
    #outputs: None
    def insert(self, word, embedding):
        new_word = WordEmbedding(word, embedding)
        self.insert1(new_word)
            
    def insert1(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        #b = self.h2(k.word)
        #b = self.h1(k.word)
        b = self.h4(k.word)
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end
    
    #print_table() - prints the table
    #only downside is that it shows all the contents as 
    #a WordEmbedding object        
    def print_table(self):
        print('Table contents:')
        for b in self.bucket:
            print(b)
            
    
    
    
    
    