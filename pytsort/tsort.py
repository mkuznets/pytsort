def add_nodes(graph, node, node2=None):
    if node not in graph:
        graph[node] = set()
    if node2 is not None:
        graph[node].add(node2)
        add_nodes(graph, node2)


def dfs(node, visited_nodes, graph, order, path=set()):
    visited_nodes[node] = True
    res = True
    for n in graph[node]:
        if n in path:
            return False
        if not visited_nodes[n]:
            res = dfs(n, visited_nodes, graph, order, path | {node})
            if not res:
                return False
    order.append(node)
    return res


def topological_sort(graph):
    visited_nodes = {node: False for node in graph}
    order = []
    for node in graph:
        if not visited_nodes[node]:
            res = dfs(node, visited_nodes, graph, order, set())
            if not res:
                return None
    return order


def tsort(strings):
    nodes = strings.split()
    if len(nodes) % 2 != 0:
        raise ValueError('Odd number of nodes. Can\'t form pairs.')
    graph = {}
    for i in range(0, len(nodes), 2):
        add_nodes(graph, nodes[i], nodes[i + 1])
    res = topological_sort(graph)
    if res is None:
        return res
    res.reverse()
    return res
