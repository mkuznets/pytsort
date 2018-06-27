# coding=utf-8

import sys
import argparse

parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')
    
def graph (text):
    nodes = text.split(' \n')
    try:
        branches = [(nodes[i], nodes[i+1]) for i in range(0, len(nodes)-1, 2)]
    except:
        raise ValueError('Odd number of nodes')
    
    g = dict()
    for n in nodes:
        g[n] = list()
        for b in branches:
            if b[0] is n:
                g[n].append(b[1])
    return g
 
    
def sort(graph):
    order = list()
    time_in = set(graph.keys())
    visited = dict()
    
    def status(node):
        visited[node] = False
        
        for n in graph[node]:            
            if n in visited:
                continue
            time_in.remove(n)
            status(n)
            
        order.append(node)
        visited[node] = True
    
    while time_in:
        status(time_in.pop())
        
    return order
    
def main():

    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read()    
    g = graph(text)
    
    return sort(g)
