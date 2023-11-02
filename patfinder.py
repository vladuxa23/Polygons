from collections import deque
from typing import Hashable, Mapping, Union, List

import networkx as nx
import matplotlib.pyplot as plt
import examples
from field import Field
from point import FieldPoint


def bfs(g: nx.Graph) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order
    Выполняет поиск в ширину и возвращает список узлов в порядке посещения

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """

    # draw_graph(g)
    start_node = list(g.nodes.keys())[0]
    path_nodes = []  # сгоревшие узлы в порядке их сгорания
    visited_nodes = {node: False for node in g.nodes}

    wait_nodes = deque()  # очередь из горящих узлов, ожидающих поджечь своих соседей
    wait_nodes.append(start_node)
    visited_nodes[start_node] = True

    while wait_nodes:
        current_node = wait_nodes.popleft()  # забираем горящий узел с начала очереди
        neighbours = g[current_node]

        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour)  # конец очереди справа
                visited_nodes[neighbour] = True

        path_nodes.append(current_node)

    # print(g, start_node)

    return


if __name__ == '__main__':

    field = Field(examples.labirynt)

    path = []
    points = []

    for row in field.points:
        for point in row:
            if point.fill == ".":
                path.append(point)
            points.append(point)
    # print(path)
    #
    # for x in range():
    #
    #     pass
    graph = nx.Graph()
    # graph.add_nodes_from(points)
    try:
        for edge in range(len(path)):
            graph.add_node(path[edge])
            graph.add_edge(path[edge], path[edge+1])
    except IndexError:
        pass


    # print(graph)

    # nx.draw_spring(graph, node_color='red', node_size=1000, with_labels=True)
    # plt.show()
    print(bfs(graph))  # {1: 0, 2: 7, 3: 9, 6: 11, 4: 20, 5: 26}
