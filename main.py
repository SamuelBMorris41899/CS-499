# provides 1 possible solution for 5.2 exercise 10
# need to find a way to get all possible solutions
edges = {"a": ["c", "b"], "c": ["f", "e"], "b": ["d"], "f": ["g"], "e": ["d"], "d": [], "g": []}
vertices = ["a", "c", "b", "f", "e", "d",  "g"]


def topological_sort(start_node, visited_array, sorted_array):

    #sets current node to starting node
    current = start_node
    # add current to visited_array and gets its neighbors
    visited_array.append(current)
    neighbors = edges[current]

    for neighbor in neighbors:
        # checks the neighbors neraby nodes(neighbor) to see if they are visited
        if neighbor not in visited_array:
            sorted_array = topological_sort(neighbor, visited_array, sorted_array) #loops itself

    # if all neighbors are visited make new starting point be current
    sorted_array.append(current)

    # if all vertices haven't been visited chooses one that isnt visited to go to
    if len(visited_array) != len(vertices):
        for vertice in vertices:
            if vertice not in visited_array:
                sorted_array = topological_sort(vertice, visited_array, sorted_array)

    # return sort
    return sorted_array


if __name__ == "__main__":
    sort = topological_sort("a", [], [])
    print(sort)