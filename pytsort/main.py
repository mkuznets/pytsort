# coding=utf-8

import sys
import argparse
import re
from collections import defaultdict


parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')


def dfs(v):

    color[v] = 'grey'

    for u in structure[v]:
        if color[u] == 'white':
            dfs(u)

    color[v] = 'black'
    done.append(v)


def topological_sort(text):

    text = re.sub('\s+|\n+', ' ', text)
    lst = text.split()

    global structure
    structure = defaultdict(list)

    for i in range(0, len(lst), 2):
        structure[lst[i]].append(lst[i + 1])

    global color
    color = defaultdict(lambda: 'white')

    global done
    done = []

    dfs(lst[0])

    return list(reversed(done))


def main():

    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read()

    for elem in topological_sort(text):
        print(elem)

