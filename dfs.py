graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ["I"],
    'E': [],
    "F": [],
    'G': [],
    "I": []
}

#dfs without recursion
def dfs(visited, graph, currentNode):
    stack = []
    stack.append(currentNode)

    while stack:
        s = stack.pop()
        if s in visited:
            continue
        visited.append(s)
        print(s)
        for i in range(len(graph[s]), 0, -1):
            stack.append(graph[s][i-1])


dfs([], graph, 'A')