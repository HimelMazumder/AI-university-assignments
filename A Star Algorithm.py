from collections import OrderedDict
from queue import PriorityQueue

print("n: ")
print("Total nodes:")
n = int(input())

# print(n)

mp = OrderedDict()

print("Enter nodes: ")
print("e.g S A B C D")
nodes = input().split()

i = 0
for node in nodes:
    mp[str(i)] = node
    i += 1

'''
for key, value in mp.items():
    print(key, value, type(key), type(value))
'''

# creating separate lists for keys and values of dictionary
val_list = list(mp.values())
key_list = list(mp.keys())

adj_matrix = []

# initializing the adjacency matrix
for r in range(n):
    tmp_lst = []
    for c in range(n):
        tmp_lst.append(0)

    adj_matrix.append(tmp_lst)

# print(adj_matrix)
# taking input in adjacency matrix
for i in range(n):
    print(f'{mp[str(i)]} connected to: ')
    if i == 0:
        print("e.g. A B")
    elif i == 1:
        print("e.g. B C D")
    elif i == 2:
        print("e.g. C")
    elif i == 3:
        print("e.g. D")
    elif i == 4:
        print("e.g. ENTER (for nodes with no arcs)")

    connected_nodes = input().split()
    if len(connected_nodes) != 0:
        print("weights: ")
        if i == 0:
            print("e.g. 1 4")
        elif i == 1:
            print("e.g. 2 5 12")
        elif i == 2:
            print("e.g. 2")
        elif i == 3:
            print("e.g. 3")

        weights = input().split()

        j = 0
        for item in connected_nodes:
            k = val_list.index(item)
            adj_matrix[i][int(key_list[k])] = int(weights[j])

            j += 1

print("Adjacency Matrix: ")
print(adj_matrix)
print()

# taking input for heuristic values of nodes
heuristic_list = []

print("Heuristics: ")
print("e.g. 7 6 2 1 0")
heuristics = input().split()

for heuristic in heuristics:
    heuristic_list.append(int(heuristic))

print()
print("Heuristics: ")
print(heuristic_list)
print()

print("Enter goal node: ")
print("e.g. D")

goal_node = input()
k = val_list.index(goal_node)
goal_node = int(key_list[k])


# print(goal_node)
# creating class for paths
class Path:
    current_node = 0
    path = ""
    heu = 0
    act = 0
    fn = 0

    def __init__(self, current_node, path, heu, act):
        self.path = path
        self.current_node = current_node
        self.heu = heu
        self.act = act
        self.fn = self.act + self.heu


# declaring priority queue for storing paths
q = PriorityQueue()
# counter is used to compare paths with the same priority in the priority queue
counter = 1


# The actual A* algorithm starts from here
cn = 0
p = mp[str(cn)]
h = heuristic_list[cn]
a = 0
pt = Path(cn, p, h, a)

q.put((pt.fn, counter, pt))

while q.qsize() != 0:
    if pt.current_node == goal_node:
        print("-------------------------------------------------------------------------------------------------------")
        print("Shortest path: ")
        print(pt.path)
        print("Optimal cost: ")
        print(pt.fn)

        break

    pt = q.get()[2]
    # print(pt.current_node)

    i = 0
    for item in adj_matrix[pt.current_node]:
        if item != 0:
            cn = i
            p = pt.path + "->" + mp[str(cn)]
            h = heuristic_list[cn]
            a = pt.act + item
            ptt = Path(cn, p, h, a)

            # print(f'Priority: {ptt.fn}')
            # print(f'Path: {ptt.path}')
            counter += 1
            q.put((ptt.fn, counter, ptt))

        i += 1
