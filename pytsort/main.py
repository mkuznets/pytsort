# coding=utf-8

import sys
import argparse

parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')


def addedge(d, start, fin):
    d[start] = d.get(start, []) + [fin]
    return d

def dfs(start, d, is_visited, ans):
    is_visited[start] = True
    if start in d:
        for fin in d[start]:
            if not is_visited[fin]:
                dfs(fin, d, is_visited, ans)
    ans.append(start)

def topological_sort(d, n_of_verts):
    is_visited = [False] * n_of_verts
    ans = []
    for i in range(n_of_verts):
        if not is_visited[i]:
            dfs(i, d, is_visited, ans)
    return ans[::-1]



def main():

    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read()
    
    d = dict()
    rd = dict()
    renaming = []
    prev = None
    for i in text.split():
        if not i in rd:
            rd[i] = len(renaming)
            renaming.append(i)
        if prev is None:
            prev = rd[i]
        else:
            addedge(d, prev, rd[i])
            prev = None
    if not prev is None:
        raise ValueError("Odd amount of vertices!")
    tinds = topological_sort(d, len(renaming))
    for i in tinds:
        print(renaming[i])
    
    
