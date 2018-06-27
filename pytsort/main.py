# coding=utf-8

import sys
import argparse
from collections import deque

parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')
 
def create_graph(text):
    l = text.replace('\n',' ').split()
    all_v = set(l)
    d = {}
    for v in all_v:
        d[v] = []
    for x in range(len(l)):
        if x % 2 == 0:
            d[l[x]].append(l[x+1]) 
        else:
            continue
    return d


def t_sort(graph):
    order = []
    into = list(graph.keys())
    visited = {}

    def recursion(node):
        visited[node] = False
        for k in graph[node]:
            if k in visited:
                continue
            into.remove(k)
            recursion(k)
        order.append(node)
        visited[node] = True

    while into:
        recursion(into[-1])
        into = into[:-1]
    return list(reversed(order))


def main():
    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read()
    #text = 'a b c\nd\ne f\nb c d e'
    #text2 = '3 8\n3\n10 5 11\n7 8 7 11 8 9 11 2 11 9 11 10'
    graph = create_graph(text)
    t_sort(graph)