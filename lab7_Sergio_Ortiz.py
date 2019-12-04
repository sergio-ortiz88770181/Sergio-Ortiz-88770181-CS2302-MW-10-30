#CS 2302 Data Structures Fall 2019 MW 10:30
#Sergio Ortiz
#Assignment - Lab #7
#Instructor - Olac Fuentes
#Teaching Assistant - Anindita Nath
#December 4, 2019
#This program will showcase three different
#algorithm design techniques, randomized, backtracking,
#and dynamic programming
import connected_components as cc
import graph_AL as graph
import numpy as np

#backtrackingHamiltonian() - Takes care of all the aesthetics
#for the hamiltonian path using backtracking. Initializes all the tools
#the algorithm will use and then prints our the result and shows the 
#hamiltonian path if one exists
#inputs - None
#outputs - None
def backtrackingHamiltonian():
    new_graph = buildGraph()
    counter = 0
    path = [-1] * len(new_graph.al)
    path[0] = 0
    if findHamPath(new_graph, path, 1, counter) == False:
        print('Sorry, no Hamiltonian Path')
    else:
        print('We found the following Hamiltonian Path')
        new_graph = graph.Graph(len(path))
        for i in range(len(path) - 1):
            new_graph.insert_edge(path[i], path[i + 1])
        new_graph.insert_edge(path[-1], path[0])
        new_graph.draw()

def buildGraph():
    print('We will now build a graph!')
    size = int(input('What size do you want the graph to be? '))
    new_graph = graph.Graph(size)
    print('Begin inserting edges, negative number on source to exit')
    source = int(input('Source: '))
    dest = int(input('Destination: '))
    while source > -1:
        if source >= size:
            print('Incorrect input, try again')
            source = int(input('Source: '))
            dest = int(input('Destination: '))
        else:
            new_graph.insert_edge(source, dest)
            source = int(input('Source: '))
            dest = int(input('Destination: '))
    print('Thank you for using the graph builder, this is your graph')
    new_graph.draw()
    return new_graph
            
#buildRandomSubset() - builds a random subset of the graph,
#used for the hamiltonian path using randomization
#Will build a random subset which will be check to see if it
#is a hamiltonian path
#inputs - g: the graph from which we are trying to find a 
#            Hamiltonian Path
#outputs - a subset of the graph, represented as an adjacency list
def buildRandomSubset(g):
    subset = graph.Graph(len(g.al))
    hash_map = {}
    for i in range(len(g.al)):
        hash_map[i] = []
    counter = len(g.al) + 1
    while counter >= 0:
        pos1 = np.random.randint(0, len(g.al))
        if len(g.al[pos1]) == 0:
            counter -= 1
        else:
            pos2 = np.random.randint(0, len(g.al[pos1]))
            if not(g.al[pos1][pos2].dest in hash_map[pos1]):
                hash_map[pos1].append(g.al[pos1][pos2].dest)
                counter -= 1
                subset.insert_edge(pos1, g.al[pos1][pos2].dest)
    return subset

#conditions() - conditions to keep the Hamiltonian path cycle,
#used in the backtrackign algorithm to see if each added edge 
#is valid to keep the Hamiltonian Cycle property
#inputs - g: the graph where we are trying to find the path
#         v: the vertex we are checking to see if it is valid
#         pos: the current position of the path
#         path: the current hamiltonian path
#         counter: used to access the correct position in the
#                  path list
#outputs - True if the vertex does not break the Hamiltonian 
#          Path, False else
def conditions(g, v, pos, path, counter):
    flag = False
    for i in range(len(g.al[path[counter]])):
        if g.al[path[counter]][i].dest == v:
            flag = True
    if not flag:
        return False
    for ver in path:
        if ver == v:
            return False
    return True

#dynamicEditDistance() - initilizes the dynamic edit
#distance problem by asking the user for two words
#inputs - None
#ouputs - None
def dynamicEditDistance():
    print()
    print('Which two words would you like to use?')
    word1 = input('Word 1: ')
    word2 = input('Word 2: ')
    editDistance(word1, word2)
    
#editDistance() - the same distance problem but 
#only swaps characters if they are both vowels or both 
#consonants
#inputs - s1: the first word
#         s2: the second word
#outputs - the distance between the two words, considering 
#that different letters only count if they are both vowels
#or both consonants
def editDistance(s1,s2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    hash_map1 = {}
    for letter in s1:
        if letter in hash_map1:
            hash_map1[letter] += 1
        else:
            hash_map1[letter] = 1
    hash_map2 = {}
    for letter in s2:
        if letter in hash_map2:
            hash_map2[letter] += 1
        else:
            hash_map2[letter] = 1
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] ==s2[j-1]:
                d[i,j] =d[i-1,j-1]
            else:
                if hash_map1[s1[i-1]] < 0 or hash_map2[s2[j-1]] < 0:
                    n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                    d[i,j] = min(n)+1
                else:
                    if s1[i - 1] in vowels and s2[j - 1] in vowels:
                        n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                        d[i,j] = min(n)+1
                    elif not(s1[i - 1] in vowels) and not(s2[j - 1] in vowels):
                        n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                        d[i,j] = min(n)+1
                    else:
                        d[i,j] =d[i-1,j-1]
            hash_map1[s1[i-1]] -= 1
            hash_map2[s2[j-1]] -= 1
    print()
    print('The distance between ',s1,' and ',s2,' is ',d[-1,-1])
    return d[-1,-1]

#findHamPath() - the actual algorithm that finds a 
#Hamiltonian Path using backtracking
#inputs   g: the graph where we are trying to find the path
#         v: the vertex we are checking to see if it is valid
#         pos: the current position of the path
#         path: the current hamiltonian path
#         counter: used to access the correct position in the
#                  path list
#outputs - True if Hamiltonian Path Found, False otherwise
def findHamPath(g, path, position, counter):
    if counter == len(g.al) - 1:
        for i in range(len(g.al[path[-1]])):
            if g.al[path[-1]][i].dest == 0:
                return True
        return False
    vertices = []
    for j in g.al[path[counter]]:
        vertices.append(j.dest)
    for j in  vertices:
        a = conditions(g, j, position, path, counter)
        if a:
            path[position] = j
            counter += 1
            if findHamPath(g, path, position + 1, counter):
                return True
            path[position] = -1
            counter -= 1
    return False

#main() - the main method where user can choose what algorithm design 
#technique to see
#inputs - None
#outputs - None
def main():
    print('Which algorithm design technique would you like to see?')
    algo = int(input('(1) Randomized, (2) Backtracking, (3) Dynamic '))
    while(algo < 1 or algo > 3):
        algo = int(input('Please enter a correct input '))
    if algo == 1:
        randomHam()
    elif algo == 2:
        backtrackingHamiltonian()
    elif algo == 3:
        dynamicEditDistance()
        
#randomHam() - Displays wheter we found a Hamiltonian Cycle
#or not
#inputs - None
#outputs - None
def randomHam():
    new_graph = buildGraph()
    subset = randomizedHamiltonian(new_graph)
    if subset is None:
        print('Your graph has no hamiltonian cycle')
    else:
        print('Your graph has the following hamiltonian cycle')
        subset.draw()
        
#randomizedHamiltonian() - builds a random subset of thhe graph
#and checks if it is a Hamiltonian Cycle
#inputs - g: the graph we are searching a Hamiltonian Cycle in
#outputs - the Hamiltonian Cycle is we find one, None otherwise
def randomizedHamiltonian(g):
    for i in range(1000):
        subset = buildRandomSubset(g)
        flag = True
        new_set = set()
        for i in range(len(subset.al)):
            for j in range(len(subset.al[i])):
                new_set.add(subset.al[i][j].dest)
            if len(new_set) != 2:
                flag = False
                break
            else:
                new_set.clear()
            
        f, n = cc.connected_components(subset)
        if f == 1 and flag:
            return subset
    return None

if __name__ == '__main__':
    main()