import random

from Node import Node

tsp_path = "Data/komiwojazer.txt"


def read_file(path):
    ffile = open(path, 'r')
    arr = list()
    for line in ffile:
        arr.append(line.replace("\n", ""))
    return arr


def sort_file(arr):
    n = 0
    tmp_arr = list()
    for i in range(len(arr)):
        if i == 0:
            n = int(arr[0])
        else:
            numbers = arr[i].split(" ")
            node = Node(int(numbers[0]), int(numbers[1]), int(numbers[2]))
            tmp_arr.append(node)
    return tmp_arr, n


def turn_list_into_graph(arr, n):
    graph = [[float('inf')] * n for _ in range(n)]

    for node in arr:
        from_node = node.from_where
        to_node = node.to_where
        distance = node.distance
        graph[from_node][to_node] = distance
        if from_node != to_node:
            graph[to_node][from_node] = distance

    for i in range(n):
        graph[i][i] = 0

    return graph


def get_neighbours(path):
    neighbours = []
    length = len(path)
    for i in range(1, length):
        for j in range(1, i):
            neighbour = path[:]
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbours.append(neighbour)
    return neighbours


def get_distance(path, table):
    distance = sum(table[path[i]][path[i + 1]] for i in range(len(path) - 1))
    distance += table[path[-1]][path[0]]
    return distance


def travelling_salesman_problem(path, graph):
    counter = 0
    best_weight = float('inf')
    best_path = None

    while True:
        counter += 1
        print(f"\nIteration number: {counter}\n")

        current_weight = get_distance(path, graph)
        if current_weight < best_weight:
            best_weight = current_weight
            best_path = path

        neighbours = get_neighbours(path)
        next_path = None
        for neighbour in neighbours:
            neighbour_weight = get_distance(neighbour, graph)
            if neighbour_weight < best_weight:
                best_weight = neighbour_weight
                next_path = neighbour

        if next_path is None:
            print("\nThe best path was found")
            return best_weight, best_path
        else:
            path = next_path
            print(f"\nBest path so far: {best_path}\nBest weight so far: {best_weight}\n")


tsp_arr = read_file(tsp_path)
tsp_list, number_of_nodes = sort_file(tsp_arr)
source_node = random.randint(0, number_of_nodes-1)
nodes_graph = turn_list_into_graph(tsp_list, number_of_nodes)
starting_path = [i for i in range(number_of_nodes)]
random.shuffle(starting_path)
answer_weight, answer_path = travelling_salesman_problem(starting_path, nodes_graph)
print(f"\n\nFor {number_of_nodes} nodes the best path is: {answer_path}, with a weight: {answer_weight}")
