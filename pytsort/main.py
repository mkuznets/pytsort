# coding=utf-8

import sys
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')

def get_graph(text):
    text = text.split()
    n = len(text)
    if n % 2 == 1: raise ValueError('Нечетное число вершин в списке!')
    #text = [(text[i], text[i+1]) for i in range(0, n, 2)]
    V = {v:[float('-inf'), float('-inf')] for v in text}
    graph = defaultdict(list)
    V_out = set(V)
    for i in range(0, n, 2):
        graph[text[i]].append(text[i+1])
        V_out.remove(text[i+1])
    return graph, V, V_out

def sorting(graph, V, V_out):
    def _sorting(node):
        nonlocal stack, seen, graph, V, time
        V[node][0] = time
        time += 1
        seen.update(node)
        stack.append(node)
        #s = True
        if node in graph:
            for i in graph[node]:
                if i not in seen:
                    #s = False
                    _sorting(i)
        V[node][1] = time
        time += 1
    stack = []
    seen = set()
    time = 0
    for i in V_out:
        if i not in seen:
            _sorting(i)
    return sorted(V, key=V.get)
    
def main():

    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read()
    graph, V, V_out = get_graph(text)
    return sorting(graph, V, V_out)
