import random


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
    while edge_count > 0:
        isolated_vertex = get_isolated_vertex(matrix)
        if isolated_vertex:
            create_edge(matrix, isolated_vertex)
            isolated_vertex = 0
        else:
            random_vertex = random.randint(0, vertex_count-1)
            create_edge(matrix, random_vertex)
        edge_count -= 1
    print_matrix(matrix)


def get_isolated_vertex(matrix):
    len_matrix = len(matrix)
    for x in range(len_matrix):
        row_sum = 0
        for y in range(len_matrix):
            row_sum += matrix[x][y]
        if row_sum == 0:
            return x


def create_edge(matrix, start_vertex):
    len_matrix = len(matrix)
    end_vertex = random.randint(0, len_matrix-1)
    while end_vertex == start_vertex or matrix[start_vertex][end_vertex] != 0:
        end_vertex = random.randint(0, len_matrix-1)
    min_random_value = 1
    max_random_value = 20
    value = random.randint(min_random_value, max_random_value)
    matrix[start_vertex][end_vertex] = value
    matrix[end_vertex][start_vertex] = value


def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


main()
