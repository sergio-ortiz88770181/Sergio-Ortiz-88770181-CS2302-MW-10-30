# Edge list representation of graphs
#Edited by Sergio Ortiz 
#Edited methods are commented
import numpy as np
import matplotlib.pyplot as plt
import math
import graph_AL as graph
import graph_AM_Sergio_Ortiz as graph1
from scipy.interpolate import interp1d

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self,  vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    #as_AL() - returns an adjacency list representation of the graph
    #inputs - None
    #outputs - an adjacency list representation of the graph
    def as_AL(self):
        g = graph.Graph(self.vertices, self.weighted, self.directed)
        for i in range(len(self.el)):
            g.insert_edge(self.el[i][0], self.el[i][1], self.el[i][2])
        return g
    
    #as_AM() - returns an adjacency matrix representation of the graph
    #inputs - None
    #outputs - an adjacency matrix representaion of the graph
    def as_AM(self):
        g = graph1.Graph(self.vertices, self.weighted, self.directed)
        for i in range(len(self.el)):
            g.insert_edge(self.el[i][0], self.el[i][1], self.el[i][2])
        return g
    
    def as_EL(self):
        return self
    
    #bfs() - does breath first search on graph
    #inputs - start vertex: where we want the bfs to start
    #outputs - discovered_set : every vertex dissovered
    #        - also prints out path so we can see where it went
    def bfs(self, start_vertex):
        new_graph = self.as_AL()
        return new_graph.bfs(start_vertex)
    
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
        for i in range(len(self.el)):
            if self.el[i][0] == source:
                if self.el[i][1] == dest:
                    self.el.pop(i)
                    return
                
    #dfs() - does depth first search on graph
    #inputs - start vertex: where we want the dfs to start
    #outputs - discovered_set : every vertex dissovered
    #        - also prints out path so we can see where it went
    def dfs(self, start_vertex):
        new_graph = self.as_AL()
        return new_graph.dfs(start_vertex)
    
    #display() - prints out the contents of the matrix
    #inputs - None
    #outputs - None 
    def display(self):
        print('[',end='')
        for i in range(len(self.el)):
            #print('[',end='')
            print('('+str(self.el[i][0])+','
                    +str(self.el[i][1])+','
                    +str(self.el[i][2])+')',end='')
            #print(']',end=' ')    
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
        if not ((dest, source, weight) in self.el):
            if not ((source, dest, weight) in self.el):
                self.el.append((source, dest, weight))
                
    
    
                
    
     
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
            