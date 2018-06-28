# coding=utf-8

import sys
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')


def make_graph(text):

    if len(text) % 2 != 0:
        raise ValueError('odd number of nodes')

    graph = defaultdict(list)
    for i in range(0, len(text), 2):
        graph[text[i]].append(text[i+1])

    return graph


def tsort(graph):

    nodes = list(graph.keys())
    visited = []

    def depth(node):
        for edge in graph[node]:
            if edge not in visited:
                depth(edge)
        if node not in visited:
            visited.append(node)

    while nodes:
        depth(nodes[0])
        del nodes[0]

    return visited[::-1]


def main():

    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read().split()

    graph = make_graph(text)
    tsorted_graph = tsort(graph)

    for node in tsorted_graph:
        print(node)
