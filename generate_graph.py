import random

MIN_EDGE_WEIGHT = 1
MAX_EDGE_WEIGHT = 20


def main():
    try:
        vertex_count = int(input())
        edge_count = int(input())
        generate_graph(vertex_count, edge_count)
    except ValueError as e:
        print(e)
        main()


def generate_graph(vertex_count, edge_count):
    if edge_count < vertex_count - 1:
        raise ValueError("Please, enter correct amount of edges")
    matrix = [[0 for x in range(vertex_count)] for y in range(vertex_count)]
    for edge in range(edge_count):
        isolated_vertex = get_isolated_vertex(matrix)
        if isolated_vertex:
            create_edge(matrix, isolated_vertex)
            isolated_vertex = 0
        else:
            random_vertex = random.randint(0, vertex_count-1)
            create_edge(matrix, random_vertex)
    print_matrix(matrix)


def get_isolated_vertex(matrix):
    for i, row in enumerate(matrix):
        if not sum(row):
            return i


def create_edge(matrix, start_vertex):
    len_matrix = len(matrix)
    end_vertex = random.randint(0, len_matrix-1)
    while end_vertex == start_vertex or matrix[start_vertex][end_vertex] != 0:
        end_vertex = random.randint(0, len_matrix-1)
    value = random.randint(MIN_EDGE_WEIGHT, MAX_EDGE_WEIGHT)
    matrix[start_vertex][end_vertex] = value
    matrix[end_vertex][start_vertex] = value


def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


main()
