# Adjacency list representation of graphs
#Edited by Sergio Ortiz 
#Edited methods are commented
import numpy as np
import matplotlib.pyplot as plt
import graph_EL_Sergio_Ortiz as graph
import graph_AM_Sergio_Ortiz as graph1
from scipy.interpolate import interp1d

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
        
    def as_AL(self):
        return self
    
    #as_AM() - returns an adjacency matrix representation of the graph
    #inputs - None
    #outputs - an adjacency matrix representation of the graph
    def as_AM(self):
        g = graph1.Graph(len(self.al), self.weighted, self.directed)
        for i in range(len(self.al)):
            for j in range(len(self.al[i])):
                g.insert_edge(i, self.al[i][j].dest, self.al[i][j].weight)
        return g
    
    #as_EL() - returns an edge list representation of the graph
    #inputs - None
    #outputs - an edge list representation of the graph
    def as_EL(self):
        g = graph.Graph(len(self.al))
        hash_map = {}
        for i in range(len(self.al)):
            hash_map[i] = []
            for j in range(len(self.al[i])):
                hash_map[i].append(self.al[i][j].dest)
                if not(self.al[i][j].dest in hash_map):
                    g.insert_edge(i, self.al[i][j].dest, self.al[i][j].weight)
                else:
                    if not(i in hash_map[self.al[i][j].dest]):
                        g.insert_edge(i, self.al[i][j].dest, self.al[i][j].weight)
        return g
    
    #bfs() - does breath first search on graph
    #inputs - start vertex: where we want the bfs to start
    #outputs - discovered_set : every vertex dissovered
    #        - also prints out path so we can see where it went
    def bfs(self, start_vertex):
        frontier_q = []
        discovered_set = []
        path = [-1 for i in range(len(self.al))]
        frontier_q.append(start_vertex)
        discovered_set.append(start_vertex)
        path[start_vertex] = start_vertex
        while len(frontier_q) != 0:
            current_v = frontier_q.pop(0)
            for i in range(len(self.al[current_v])):
                if not self.al[current_v][i].dest in discovered_set:
                    frontier_q.append(self.al[current_v][i].dest)
                    discovered_set.append(self.al[current_v][i].dest)
                    path[self.al[current_v][i].dest] = current_v
        print(path)
        return discovered_set
    
    #chicken_bfs() - solves the chicken riddle with bfs
    #inputs - start_vetrex : where we want bfs to start, should be
    #                        just 0 but i didnt know how to initialize it
    #outputs - the path to solve the chicken riddle
    def chicken_bfs(self, start_vertex):
        hash_map = {
                0 : '0000',
                1 : '0001',
                2 : '0010',
                3 : '0011',
                4 : '0100',
                5 : '0101',
                6 : '0110',
                7 : '0111',
                8 : '1000',
                9 : '1001',
                10: '1010',
                11: '1011',
                12: '1100',
                13: '1101',
                14: '1110',
                15: '1111',
                }
        frontier_q = []
        discovered_set = []
        path = [-1 for i in range(len(self.al))]
        frontier_q.append(start_vertex)
        discovered_set.append(start_vertex)
        path[start_vertex] = start_vertex
        while len(frontier_q) != 0:
            current_v = frontier_q.pop(0)
            for i in range(len(self.al[current_v])):
                if not self.al[current_v][i].dest in discovered_set:
                    if hash_map[self.al[current_v][i].dest][-1] == '0':
                        if not(hash_map[self.al[current_v][i].dest][0] == '1' and hash_map[self.al[current_v][i].dest][1] == '1'):
                            if not(hash_map[self.al[current_v][i].dest][1] == '1' and hash_map[self.al[current_v][i].dest][2] == '1'):
                                frontier_q.append(self.al[current_v][i].dest)
                                discovered_set.append(self.al[current_v][i].dest)
                                path[self.al[current_v][i].dest] = current_v
                    if hash_map[self.al[current_v][i].dest][-1] == '1':
                        if not(hash_map[self.al[current_v][i].dest][0] == '0' and hash_map[self.al[current_v][i].dest][1] == '0'):
                            if not(hash_map[self.al[current_v][i].dest][1] == '0' and hash_map[self.al[current_v][i].dest][2] == '0'):
                                frontier_q.append(self.al[current_v][i].dest)
                                discovered_set.append(self.al[current_v][i].dest)
                                path[self.al[current_v][i].dest] = current_v
        returning_path = []
        returning_path.append(len(path) - 1)
        search_val = path[-1]
        while search_val != 0:
            returning_path.insert(0, search_val)
            search_val = path[search_val]
        returning_path.insert(0, search_val)
        return returning_path
    
    #chicken_dfs() - solves the chicken riddle using dfs
    #inputs - start_vetrex : where we want bfs to start, should be
    #                        just 0 but i didnt know how to initialize it
    #outputs - the path to solve the chicken riddle
    def chicken_dfs(self, start_vertex):
        hash_map = {
                    0 : '0000',
                    1 : '0001',
                    2 : '0010',
                    3 : '0011',
                    4 : '0100',
                    5 : '0101',
                    6 : '0110',
                    7 : '0111',
                    8 : '1000',
                    9 : '1001',
                    10: '1010',
                    11: '1011',
                    12: '1100',
                    13: '1101',
                    14: '1110',
                    15: '1111',
                    }
        stack = []
        visited_set = []
        stack.append(start_vertex)
        path = [-1 for i in range(len(self.al))]
        path[start_vertex] = start_vertex
        while len(stack) != 0:
            current_v = stack.pop()
            if not current_v in visited_set:
                for i in range(len(self.al[current_v])):
                    if hash_map[self.al[current_v][i].dest][-1] == '0':
                        if not(hash_map[self.al[current_v][i].dest][0] == '1' and hash_map[self.al[current_v][i].dest][1] == '1'):
                            if not(hash_map[self.al[current_v][i].dest][1] == '1' and hash_map[self.al[current_v][i].dest][2] == '1'):
                                visited_set.append(current_v)
                                stack.append(self.al[current_v][i].dest)
                                if not self.al[current_v][i].dest in visited_set:
                                    path[self.al[current_v][i].dest] = current_v
                    if hash_map[self.al[current_v][i].dest][-1] == '1':
                        if not(hash_map[self.al[current_v][i].dest][0] == '0' and hash_map[self.al[current_v][i].dest][1] == '0'):
                            if not(hash_map[self.al[current_v][i].dest][1] == '0' and hash_map[self.al[current_v][i].dest][2] == '0'):
                                visited_set.append(current_v)
                                stack.append(self.al[current_v][i].dest)
                                if not self.al[current_v][i].dest in visited_set:
                                    path[self.al[current_v][i].dest] = current_v
        returning_path = []
        returning_path.append(len(path) - 1)
        search_val = path[-1]
        while search_val != 0:
            returning_path.insert(0, search_val)
            search_val = path[search_val]
        returning_path.insert(0, search_val)
        return returning_path
    
    def delete_edge(self,source,dest):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')
            
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    
    #dfs() - does depth first search on graph
    #inputs - start vertex: where we want the dfs to start
    #outputs - discovered_set : every vertex dissovered
    #        - also prints out path so we can see where it went
    def dfs(self, start_vertex):
        stack = []
        visited_set = []
        stack.append(start_vertex)
        path = [-1 for i in range(len(self.al))]
        path[start_vertex] = start_vertex
        while len(stack) != 0:
            current_v = stack.pop()
            if not current_v in visited_set:
                visited_set.append(current_v)
                for i in range(len(self.al[current_v])):
                    stack.append(self.al[current_v][i].dest)
                    if not self.al[current_v][i].dest in visited_set:
                        path[self.al[current_v][i].dest] = current_v
        print(path)
        return visited_set
    
    def display(self):
        print('[',end='')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']') 
                
    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
        
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest,weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source,weight))
    
    
    
          
            
      
     
    
            
    
        
    
    
                
    
    
    
    
    
    
    
    
    
    