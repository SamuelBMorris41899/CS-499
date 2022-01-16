import numpy as np
import networkx as nx
import math
from graphviz import Source





def main():
    choice = int(input("Do you want to (1) find a graph from an adjacency matrix, (2) an adjacency matrix from a graph, or (3) An adjacency list from a graph? Enter 1, 2, or 3: "))
    if choice == 1:
        adjMatrixInput()
    elif choice == 2:
        graphInput(choice)
    elif choice == 3:
        graphInput(choice)
    else:
        main()






def graphInput(choice):
    graph = input("Enter edges in the format (N1, N2) where N is a node. Separate multiple edges with a comma: ")
    directed = input("Is this a directed graph? y/n: ")

    createGraph(eval("[%s]" % graph.strip(" ")), directed, choice)


def createGraph(graph, directed, choice):
    if directed.lower() == 'y':
        g = nx.MultiDiGraph()
    if directed.lower() == 'n':
        g = nx.MultiGraph()
    #Else retry input

    g.add_edges_from(graph)

    if choice == 2:
        computeAdjMatrix(g)
    elif choice == 3:
        printAdjList(g)


def computeAdjMatrix(g):
    Adj = nx.to_numpy_matrix(g, nodelist=sorted(g.nodes()))
    print(Adj)


def computeAdjList(g, delimiter=" "):
    init = []
    line = []
    for s, nbrs in g.adjacency():
        init.clear()
        line.clear()
        init.append(s)
        for t, data in nbrs.items():
            line.append(t)
        line.sort()
        adjList = init + line
        adjList = " ".join(str(x) for x in adjList)
        yield adjList

def printAdjList(g):
    h = nx.Graph()
    h.add_nodes_from(sorted(g.nodes(data=True)))
    h.add_edges_from(g.edges(data=True))
    for adjList in computeAdjList(h):
        print(adjList)

def adjMatrixInput():
    Adj = input("Enter the rows of an adjacency matrix in the format [X, Y, Z], [X1, Y1, Z1], ...: ")
    Directed = input("Directed? y/n: ")

    if 'x' in Adj:
        Adj = Adj.replace("x", "0")
        Adj = np.matrix(Adj)
        n = max(Adj.shape)
        sqrt = int(math.sqrt(n))
        square = Adj.reshape((sqrt, sqrt))
        square = square + square.T - np.diag(np.diag(square))
    else:
        Adj = np.matrix(Adj)
        n = max(Adj.shape)
        sqrt = int(math.sqrt(n))
        square = Adj.reshape((sqrt, sqrt))

    print(square)
    createAdjMatrix(square, Directed)


def createAdjMatrix(squareMatrix, directed):
    if directed == 'y':
        g = nx.from_numpy_matrix(squareMatrix, parallel_edges=True, create_using=nx.MultiDiGraph)
    elif directed == 'n':
        g = nx.from_numpy_matrix(squareMatrix, parallel_edges=True, create_using=nx.MultiGraph)

    drawGraph(g)


def drawGraph(g):
    nx.drawing.nx_pydot.write_dot(g, 'multi.dot')
    renderGraph()


def renderGraph():
    path = 'multi.dot'
    s = Source.from_file(path)
    print(s.source)

    s.render('multi.dot', format='jpg', view=True)

main()
