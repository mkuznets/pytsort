# coding=utf-8

import sys
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='perform topological sort')

parser.add_argument('infile', nargs='?', metavar='FILE',
                    type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--version', dest='version', action='store_true',
                    help='output version information and exit')


#делаем граф из заданных вершин
def graph(text):
	text = text.split()
	n = len(text)
	if n % 2 == 1:
		raise ValueError('Задано нечётное число вершин')

	full_graph = defaultdict(list)

	for i in range(0, n, 2):
		full_graph[text[i]].append(text[i+1])
		
	return full_graph
	
#готовим пустой массив для использованных вершин	
def topological_sorting(full_graph):
	used = []
	vertices = list(full_graph.keys())
	
	#проход в глубину
	def down_graph(vertex):
		for i in full_graph[vertex]:
			if i not in used:
				down_graph(i)
		if vertex not in used:
			used.append(vertex)
			
	#проходим в глубину от каждой вершины в списке вершин vertices
	for i in vertices:
		down_graph(vertices[0])
		vertices.remove(i)
	return used[::-1]


def main():

    args = parser.parse_args()

    if args.version:
        print('pytsort @ HSE Algorithms S18')
        return 0

    text = args.infile.read()
    full_graph = graph(text)
    graph_sorted = topological_sorting(full_graph)
    for i in graph_sorted:
    	print(i)
    	
