from graph import *


# A Python3 program to find size of minimum
# vertex cover using Binary Search

# Returns true if there is a possible subSet
# of size 'k' that can be a vertex cover
def isCover(graph, k):
    V = len(graph.nodes)
    E = len(graph.edges_set)

    # Set has first 'k' bits high initially
    Set = (1 << k) - 1

    limit = (1 << V)

    # to mark the edges covered in each
    # subSet of size 'k'
    vis = [[None] * V for i in range(V)]

    while (Set < limit):

        # Reset visited array for every
        # subSet of vertices
        vis = [[0] * V for i in range(V)]

        # Set counter for number of edges covered
        # from this subSet of vertices to zero
        cnt = 0

        # selected vertex cover is the
        # indices where 'Set' has its bit high
        j = 1
        v = 0
        while(j < limit):
            if (Set & j):

                # Mark all edges emerging out of
                # this vertex visited
                for k in graph.edges[v]:
                    if (not vis[v][k]):
                        vis[v][k] = 1
                        vis[k][v] = 1
                        cnt += 1
            j = j << 1
            v += 1

        # If the current subSet covers all the edges
        if (cnt == E):
            return True

        # Generate previous combination with k bits high
        # Set & -Set = (1 << last bit high in Set)
        c = Set & -Set
        r = Set + c
        Set = (((r ^ Set) >> 2) // c) | r
    return False

# Returns answer to graph stored in Graph object
def findMinCover(graph):
    # Binary search the answer
    left = 1
    right = len(graph.nodes)
    while (right > left):
        mid = (left + right) >> 1
        if (isCover(graph, mid) == False):
            left = mid + 1
        else:
            right = mid

    # at the end of while loop both left and
    # right will be equal, as when they are
    # not, the while loop won't exit the
    # minimum size vertex cover = left = right
    return left

