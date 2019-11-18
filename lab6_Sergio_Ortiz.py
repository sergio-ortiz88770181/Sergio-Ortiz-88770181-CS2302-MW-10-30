#CS 2302 Data Structures Fall 2019 MW 10:30
#Sergio Ortiz
#Assignment - Lab #6
#Instructor - Olac Fuentes
#Teaching Assistant - Anindita Nath
#November 15, 2019
#This program will convert between various graphs 
#implementations
#Next, it will solve the riddle:
#You have a fox, a chicken and a sack of grain. You must cross a river with only one of them at a time.
#If you leave the fox with the chicken he will eat it; 
#if you leave the chicken with the grain he will eat it. 
#How can you get all three across safely?

import graph_AL as graph
import graph_AM_Sergio_Ortiz as graph1
import graph_EL_Sergio_Ortiz as graph2

#adjacency_list() - builds an adjacency list and converts it 
#                   to all the other graph types
#inputs - None
#outputs - None
def adjacency_list():
    print('adjacency list:')
    print()
    al = show_AL()
    print()
    print('adjacency matrix')
    print()
    show_AM()
    print()
    print('adjacency list to adjacency matrix')
    print()
    al_am = al.as_AM()
    al_am.display()
    print()
    print('edge list')
    print()
    show_EL()
    print()
    print('adjacency list to edge list')
    print()
    al_el = al.as_EL()
    al_el.display()
    print()

#adjacency_matrix() - builds an adjacency matrix and converts it 
#                   to all the other graph types
#inputs - None
#outputs - None    
def adjacency_matrix():
    print('adjacency matrix:')
    print()
    am = show_AM()
    print()
    print('adjacency list')
    print()
    show_AL()
    print()
    print('adjacency matrix to adjacency list')
    print()
    am_al = am.as_AL()
    am_al.display()
    print()
    print('edge list')
    print()
    show_EL()
    print()
    print('adjacency matrix to edge list')
    print()
    am_el = am.as_EL()
    am_el.display()
    print()  
    
#chicken_breadth() - solves the chicken riddle using bfs
#inputs - g: the graph we will search
#outputs: None
def chicken_breadth(g):
    chicken_path = g.chicken_bfs(0)
    print('The path for the riddle using bfs is ')
    print(chicken_path)
    
#chicken_build_AL() - builds an adjacency list for the chicken riddle
#inputs: None
#ouputs: A graph containing all the possible moves in the chicken riddle
def chicken_build_AL():
    g = graph.Graph(16)
    g.insert_edge(0, 1)
    g.insert_edge(0, 9)
    g.insert_edge(0, 5)
    g.insert_edge(0, 3)
    g.insert_edge(2, 3)
    g.insert_edge(2, 11)
    g.insert_edge(2, 7)
    g.insert_edge(4, 5)
    g.insert_edge(4, 13)
    g.insert_edge(4, 7)
    g.insert_edge(6, 7)
    g.insert_edge(6, 15)
    g.insert_edge(8, 9)
    g.insert_edge(8, 13)
    g.insert_edge(8, 11)
    g.insert_edge(10, 11)
    g.insert_edge(10, 15)
    g.insert_edge(12, 15)
    g.insert_edge(14, 15)
    g.draw()
    return g  

#chicken_build_AM() - builds an adjacency matrix for the chicken riddle
#inputs: None
#ouputs: A graph containing all the possible moves in the chicken riddle
def chicken_build_AM():
    g = graph1.Graph(16)
    g.insert_edge(0, 1)
    g.insert_edge(0, 9)
    g.insert_edge(0, 5)
    g.insert_edge(0, 3)
    g.insert_edge(2, 3)
    g.insert_edge(2, 11)
    g.insert_edge(2, 7)
    g.insert_edge(4, 5)
    g.insert_edge(4, 13)
    g.insert_edge(4, 7)
    g.insert_edge(6, 7)
    g.insert_edge(6, 15)
    g.insert_edge(8, 9)
    g.insert_edge(8, 13)
    g.insert_edge(8, 11)
    g.insert_edge(10, 11)
    g.insert_edge(10, 15)
    g.insert_edge(12, 15)
    g.insert_edge(14, 15)
    g.draw()
    return g 

#chicken_build_EL() - builds an edge list for the chicken riddle
#inputs: None
#ouputs: A graph containing all the possible moves in the chicken riddle
def chicken_build_EL():
    g = graph2.Graph(16)
    g.insert_edge(0, 1)
    g.insert_edge(0, 9)
    g.insert_edge(0, 5)
    g.insert_edge(0, 3)
    g.insert_edge(2, 3)
    g.insert_edge(2, 11)
    g.insert_edge(2, 7)
    g.insert_edge(4, 5)
    g.insert_edge(4, 13)
    g.insert_edge(4, 7)
    g.insert_edge(6, 7)
    g.insert_edge(6, 15)
    g.insert_edge(8, 9)
    g.insert_edge(8, 13)
    g.insert_edge(8, 11)
    g.insert_edge(10, 11)
    g.insert_edge(10, 15)
    g.insert_edge(12, 15)
    g.insert_edge(14, 15)
    g.draw()
    return g 

#chicken_depth() - solves the chicken riddle using dfs
#inputs - g: the graph we will search
#outputs: None
def chicken_depth(g):
    chicken_path = g.chicken_dfs(0)
    print()
    print('The path for the riddle using dfs is ')
    print()
    print(chicken_path)
    
#edge_list() - builds an edge list and converts it 
#                   to all the other graph types
#inputs - None
#outputs - None
def edge_list():
    print('edge list:')
    print()
    el = show_EL()
    print()
    print('adjacency list')
    print()
    show_AL()
    print()
    print('edge list to adjacency list')
    print()
    el_al = el.as_AL()
    el_al.display()
    print()
    print('adjacency matrix')
    print()
    show_AM()
    print()
    print('edge list to adjacency matrix')
    print()
    el_am = el.as_AM()
    el_am.display()
    print()  
    
#main() - main method where everything happens
#inputs - None
#outputs - None
def main():
    print('(1) Adjacency List')
    print('(2) Adjacency Matrix')
    print('(3) Edge List')
    which_graph = int(input('Which graph would you like to see? '))
    print()
    while which_graph < 1 or which_graph > 3:
        which_graph = int(input('Enter a valid graph '))
    if which_graph == 1:
        adjacency_list()
    elif which_graph == 2:
        adjacency_matrix()
    else:
        edge_list()
    
    print('Now for the chicken riddle')
    print('(1) Adjacency List')
    print('(2) Adjacency Matrix')
    print('(3) Edge List')
    which_graph = int(input('Which graph would you like to use? '))
    print()
    while which_graph < 1 or which_graph > 3:
        which_graph = int(input('Enter a valid graph '))
    print()
    print('(1) Breadth First Search')
    print('(2) Depth First Search')
    which_search = int(input('Which search would you like to use? '))
    while which_search < 1 or which_search > 2:
        which_search = int(input('Enter a valid search '))
    if which_graph == 1:
        g = chicken_build_AL()
    elif which_graph == 2:
        g = chicken_build_AM()
    else:
        g = chicken_build_EL()
    
    if which_search == 1:
        chicken_breadth(g)
    else:
        chicken_depth(g)

#show_AL() - shows the adjacency list by displaying and drawing it
#inputs - None
#outputs - g: an adjacency list
def show_AL():
    g = graph.Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.delete_edge(1,2)
    g.display()
    g.draw()
    return g

#show_AM() - shows the adjacency matrix by displaying and drawing it
#inputs - None
#outputs - g: an adjacency matrix    
def show_AM():
    g = graph1.Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.delete_edge(1,2)
    g.display()
    g.draw()
    return g
    
#show_El() - shows the edge list by displaying and drawing it
#inputs - None
#outputs - g: an edge list
def show_EL():
    g = graph2.Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.delete_edge(1,2)
    g.display()
    g.draw()
    return g

    
if __name__ == "__main__":
    main()
    