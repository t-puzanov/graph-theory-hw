import bfs

def read_input():
    f = open("input.txt", "r", encoding="utf-8")
    split_row = lambda x: list(map(int, x.split(" ")))
    data = list(map(split_row, f.read().split("\n")))
    return data[0][0], data[1:]

def write_output(adjacency_matrix):
    f = open("output.txt", "w", encoding="utf-8")
    for row in adjacency_matrix:
        f.write(" ".join(map(str, row)) + "\n")

def T_to_adjacency_matrix(n, T):
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for v in T:
        x, y = v
        adjacency_matrix[x][y] = 1
        adjacency_matrix[y][x] = 1
    return adjacency_matrix


if __name__ == "__main__":
    a, adjacency_matrix, n = None, None, None

    try:
        a, adjacency_matrix = read_input()
        n = len(adjacency_matrix)
    except:
        print("Invalid input data!")
        exit()

    T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)

    write_output(T_to_adjacency_matrix(n, T))

    print("Done!")