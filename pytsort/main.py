# coding=utf-8

import sys
import argparse
from collections import deque


parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')


def parse_input(_input):
    nodes = _input.split()
    
    if len(nodes) % 2 != 0:
        print('Error: odd number of nodes', file=sys.stderr)
        return 1
    
    return [(nodes[i], nodes[i+1]) for i in range(0, len(nodes), 2)]
    

def build_adjency_dict(edges):    
    d = dict()
    
    for e in edges:
        if e[0] in d:
            d[e[0]].append(e[1])
        
        else:
            d[e[0]] = list()
            d[e[0]].append(e[1])
            
        if e[1] not in d:
            d[e[1]] = list()
    
    return d


def tsort(edges):
    def dft(node):
        for n in adj_dict[node]:
            if not visited[n]:
                parent_map[n] = node
                return n
        
        return None
    
    if not edges:
        return 0
    
    adj_dict = build_adjency_dict(edges)
    nodes = list(adj_dict.keys())
    visited = {n: False for n in nodes}
    parent_map = dict()
    grey = deque(nodes[:1])
    black = deque([])
    _sorted = deque([])
    
    for node in nodes:
        if not visited[node]:
            grey = deque([node])
            black = deque([])

            while grey:
                _node = grey[-1]

                adj_node = dft(_node)

                if adj_node is None:
                    grey.pop()
                    visited[_node] = True
                    black.append(_node)

                elif adj_node in grey:
                    cycle = [adj_node, _node]

                    _parent = parent_map[_node]

                    while _parent != adj_node:
                        cycle.append(_parent)
                        _parent = parent_map[_parent]

                    print('Error: cycle detected (%s)'
                            % ' -> '.join(cycle), file=sys.stderr
                        )

                    return 1

                else:
                    grey.append(adj_node)

            while black:
                _sorted.append(black.pop())
                
    while _sorted:
        print(_sorted.popleft(), file=sys.stdout)
    
    return 0


def main():

    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read()
    
    edges = parse_input(text)

    if not isinstance(edges, list):
        return 1
 
    tsort(edges)


if __name__ == '__main__':
    main()
