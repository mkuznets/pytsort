# coding=utf-8

import sys
import argparse

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
    edges_src = text.split()
    assert len(edges_src) % 2 == 0
    vertexes = {}
    for i in range(0, len(edges_src), 2):
        start_vertex = edges_src[i]
        end_vertex = edges_src[i+1]
        vertexes.setdefault(start_vertex, []).append(end_vertex)
    visited = {}
    exited = {}
    verts = list(vertexes.keys())
    time = 1
    while verts:
        current = verts[-1]
        print(current, verts)
        if current not in visited:
            if current in vertexes:
                verts += vertexes[current]
            visited[current] = time
            time += 1
        elif current not in exited:
            exited[current] = time
            time += 1
            verts.pop(-1)
        else:
            verts.pop(-1)
    for elem in sorted(exited.items(), key=lambda x: x[1]):
        print(elem[0])

