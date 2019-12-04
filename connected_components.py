import graph_AL as graph
import dsf

def connected_components(g):
    vertices = len(g.al)
    components = vertices
    s = dsf.DSF(vertices )
    for v in range(vertices):
        for edge in g.al[v]:
            components -= s.union(v,edge.dest)
            #s.draw()
    return components, s

if __name__ == "__main__":   
    plt.close("all")   
    g = graph.Graph(9)
    g.insert_edge(0,2)
    g.insert_edge(0,4)
    g.insert_edge(3,6)
    g.insert_edge(1,8)
    g.insert_edge(4,5)
    
    g.display()
    g.draw()
            
    n, f = connected_components(g)
    print('The graph has',n,'connected components')
    print(f.parent)
    f.draw()