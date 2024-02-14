"""
-------------------------------------------------------
Prim's Algorithm
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from Graph import Graph
from Graph import Edge

def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    edgesused = []
    i = 0
    length = len(graph)
    node = start_node
    total = 0
    edgelist = []
    edgelistremoved = []
    Nodelist = []
    Nodenames = graph.node_names()
    
    while len(Nodelist) < len(Nodenames) - 1:
      
        Nodelist.append(node)
        edges = graph.edges_by_node(node)
        
            
        q = 0
        
        while q < len(edges):
            revedge = edges[q].reverse() 
            l = 0
            d = True
            
            while d == True and  l < len(edgelist):
                if revedge.start == edgelist[l].start and revedge.end == edgelist[l].end:
                    d = False
                l += 1
            
            l = 0
            kn = True
            
            while kn == True and  l < len(edgelistremoved):
                if revedge.start == edgelistremoved[l].start and revedge.end == edgelistremoved[l].end:
                    kn = False
                l += 1
            
            
            if d == True and kn == True :
                edgelist.append(edges[q])
                pq.insert(edges[q].distance)
            q += 1

        
        shortest = pq.remove()    
        c = 0
        length2 = len(edgelist)
        while c < length2:
            if edgelist[c].distance == shortest:
                edge = edgelist[c]
                edgesused.append(edge)
                
                if edge.end in Nodelist:
                    shortest = pq.remove()
                    c = -1
                else:
                    c = len(edgelist)
  
            c += 1
        
       
        
        edgelist.remove(edge)
        
        edgelistremoved.append(edge)
        
        node = edge.end       
        i += 1
    
    edges = edgelistremoved
    
    q = 0
    
    while q < len(edgelistremoved):
        total += edgelistremoved[q].distance
        q += 1
    return edges, total
    
