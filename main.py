from Node import Node


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
            node = Node(numbers[0], numbers[1], numbers[2])
            tmp_arr.append(node)
    return tmp_arr
