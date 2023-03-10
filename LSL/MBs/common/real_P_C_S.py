import numpy as np


def real_p_c_s(k, real_graph_path):
    graph = np.zeros((k, k))
    i = 0
    for line in open(real_graph_path):
        a = line.split("  ")
        j = 0
        for n in a:
            graph[i, j] = n
            j += 1
        i += 1

    MB = [[] for i in range(k)]
    Parents = [[] for i in range(k)]
    Children = [[] for i in range(k)]
    PC = [[] for i in range(k)]
    Spouses = [[] for i in range(k)]

    for i in range(k):
        parents = [j for j in range(k) if graph[j, i] == 1]
        Parents[i] = list(set(Parents[i]).union(set(parents)))

        children = [j for j in range(k) if graph[i, j] == 1]
        Children[i] = list(set(Children[i]).union(set(children)))

        PC[i] = list(set(Parents[i]).union(set(Children[i])))

    for i in range(k):
        children = Children[i]
        for child in children:
            spouse = Parents[int(child)]
            Spouses[i] = list(set(Spouses[i]).union(set(spouse)))
        if i in Spouses[i]:
            Spouses[i].remove(i)

    for i in range(k):
        MB[i] = list(set(PC[i]).union(set(Spouses[i])))

    return Parents, Children, Spouses

# p, c, s = real_p_c_s(20)
# print(p)
# print(c)
# print(s)