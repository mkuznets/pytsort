# coding=utf-8
# Kostyanitsyna

import sys
import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')


def main():

    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read()

    def req(v, G, d, visited, i=0):

        d[v].append(i)
        i += 1

        if not G.get(v):
           d[v].append(i)
           i += 1
           visited[v] = 1
           return i

        for l in G[v]:

            if not visited.get(l):
                i = req(l, G, d, visited, i)

        d[v].append(i)
        visited[v] = 1
        i += 1
        return i

    if not isinstance(text, str):
        raise ValueError('Not str')

    if len(text) == 0:
        return

    if text[-1] == '\n':
        text = text[:-1]
    
    if len(re.split(u'\s|\u200b', text)) % 2 != 0:
        raise ValueError('not enought v')

    V = re.findall('\w\s\w', text)
    G = defaultdict(set)

    for idx, i in enumerate(V):
        v = re.split(u'\s', i)
        G[v[0]].add(v[1])

    d = defaultdict(list) # [start, finish]
    visited = defaultdict(int)

    i = 0
    
    for v in G:
        if not visited.get(v):
            i = req(v, G, d, visited, i)

    for v in sorted(d.items(), key=lambda x: x[1][1], reverse=True):
        print(v[0])
