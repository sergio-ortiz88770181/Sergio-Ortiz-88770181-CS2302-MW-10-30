# Adjacency matrix representation of graphs
#Edited by Sergio Ortiz 
#Edited methods are commented
import numpy as np
import matplotlib.pyplot as plt
import math
import graph_AL as graph
import graph_EL_Sergio_Ortiz as graph1
from scipy.interpolate import interp1d

class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int) - 1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    #as_AL() - returns an adjacency list implementation of the graph
    #inputs - None
    #outputs - an adjacency list implementation of the graph
    def as_AL(self):
        g = graph.Graph(len(self.am), self.weighted, self.directed)
        hash_map = {}
        for i in range(len(self.am)):
            hash_map[i] = []
            for j in range(len(self.am[i])):
                if self.am[i][j]!= -1:
                    if not(j in hash_map):
                        hash_map[i].append((j))
                        g.insert_edge(i, j, self.am[i][j])
                    else:
                        if not(i in hash_map[j]):
                            hash_map[i].append(j)
                            g.insert_edge(i, j, self.am[i][j])
        return g
    
    def as_AM(self):
        return self
    
    #as_EL() - returns an edge list representation of the graph
    #inputs - None
    #outputs - an edge list representation of the graph
    def as_EL(self):
        g = graph1.Graph(len(self.am), self.weighted, self.directed)
        hash_map = {}
        for i in range(len(self.am)):
            hash_map[i] = []
            for j in range(len(self.am[i])):
                if self.am[i][j]!= -1:
                    if not(j in hash_map):
                        hash_map[i].append((j))
                        g.insert_edge(i, j, self.am[i][j])
                    else:
                        if not(i in hash_map[j]):
                            hash_map[i].append(j)
                            g.insert_edge(i, j, self.am[i][j])
        return g
    
    #bfs() - does breath first search on graph
    #inputs - start vertex: where we want the bfs to start
    #outputs - discovered_set : every vertex dissovered
    #        - also prints out path so we can see where it went
    def bfs(self, start_vertex):
        frontier_q = []
        discovered_set = []
        path = [-1 for i in range(len(self.am))]
        frontier_q.append(start_vertex)
        discovered_set.append(start_vertex)
        path[start_vertex] = start_vertex
        while len(frontier_q) != 0:
            current_v = frontier_q.pop(0)
            for i in range(len(self.am[current_v])):
                if self.am[current_v][i] != -1:
                    if not i in discovered_set:
                        frontier_q.append(i)
                        discovered_set.append(i)
                        path[i] = current_v
        print(path)
        return discovered_set
    
    #chicken_bfs() - solves the chicken riddle with bfs
    #inputs - start_vetrex : where we want bfs to start, should be
    #                        just 0 but i didnt know how to initialize it
    #outputs - the path to solve the chicken riddle
    def chicken_bfs(self, start_vertex):
        new_graph = self.as_AL()
        return new_graph.chicken_bfs(start_vertex)
    
    #chicken_dfs() - solves the chicken riddle using dfs
    #inputs - start_vetrex : where we want bfs to start, should be
    #                        just 0 but i didnt know how to initialize it
    #outputs - the path to solve the chicken riddle
    def chicken_dfs(self, start_vertex):
        new_graph = self.as_AL()
        return new_graph.chicken_dfs(start_vertex)
    
    #delete_edge() - deletes an edge from the graph
    #inputs - source: the source of the edge
    #       - dest: the destination of the edge
    #outputs - None
    def delete_edge(self,source,dest):
        self.am[source][dest] = -1
        if self.directed != True:
            self.am[dest][source] = -1
            
    #dfs() - does depth first search on graph
    #inputs - start vertex: where we want the dfs to start
    #outputs - discovered_set : every vertex dissovered
    #        - also prints out path so we can see where it went
    def dfs(self, start_vertex):
        stack = []
        visited_set = []
        stack.append(start_vertex)
        path = [-1 for i in range(len(self.am))]
        path[start_vertex] = start_vertex
        while len(stack) != 0:
            current_v = stack.pop()
            if not current_v in visited_set:
                visited_set.append(current_v)
                for i in range(len(self.am[current_v])):
                    if self.am[current_v][i] != -1:
                        stack.append(i)
                        if not i in visited_set:
                            path[i] = current_v
        print(path)
        return visited_set
    
    #display() - prints out the contents of the matrix
    #inputs - None
    #outputs - None            
    def display(self):
        print('[',end='')
        for i in range(len(self.am)):
            print('[',end='')
            for edge in self.am[i]:
                print('('+str(edge)+')' ,end='')
            print(']',end=' ')
            print()
        print(']') 
                
    #draw() - draws the graph
    #inputs - None
    #outputs - None
    def draw(self):
        al = self.as_AL()
        al.draw()
        
    #insert_edge() - inserts an edge to the graph
    #inputs - source: the source of the edge
    #       - dest: the destination of the edge
    #       - weight : the weight of the edge
    #outputs - None
    def insert_edge(self,source,dest,weight=1):
        self.am[source][dest] = weight
        if self.directed != True:
            self.am[dest][source] = weight
        
    
    
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
            
