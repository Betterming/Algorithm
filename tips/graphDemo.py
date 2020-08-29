"""
python 表示图结构
    A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C
"""

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.



if __name__ == '__main__':
    # 未知不带权用字典+数组表示
    # 带权用字典+字典表示
    #
    graph1 = {
        'A': {'B':1, 'C':2},
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }
    a, b, c, d, e, f = range(6)
    graph2 = [
        {a:2, b:3},

    ]
    find_path(graph1, 'A', 'F')



