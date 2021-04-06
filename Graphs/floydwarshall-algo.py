import argparse
import os
import sys


def FloydWarshall(m, vertex):
    V = vertex
    dist = [[0] * V for i in range(V)]
    nxt = [[0] * V for i in range(V)]
    for i in range(0, V):
        for j in range(0, V):
            dist[i][j] = 0

    for i in range(0, V):
        for j in range(0, V):
            dist[i][j] = m[i][j]

    for i in range(0, V):
        for j in range(0, V):
            if i != j:
                nxt[i][j] = j + 1

    for k in range(0, V):
        for i in range(0, V):
            for j in range(0, V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]

    printShortPath(dist, V, nxt)


def printShortPath(dist, V, nxt):
    print("\nVertices  Weight   Minimum Short Path")
    for i in range(0, V):
        for j in range(0, V):
            if i != j:
                u = i + 1
                v = j + 1
                if dist[i][j] == float("inf"):
                    path = "(%d, %d)     -       No path between %d and %d" % (
                        u,
                        v,
                        u,
                        v,
                    )
                else:
                    path = "(%d, %d)     %2d       %s" % (u, v, dist[i][j], u)
                    while True:
                        if u != v:
                            u = nxt[u - 1][v - 1]
                            path += " -> " + str(u)
                        else:
                            break
                print(path)
        print()


def checkFile(f):
    v = f.readline().rstrip()
    if not v.isnumeric():
        print(
            "Invalid input file format: The first line must contain an integer (number of vertices)!"
        )
        exit(1)
    if sum(1 for line in f) != int(v):
        print("Invalid input file format: Incompatible matrix size!")
        exit(1)
    f.seek(2)
    for line in iter(f):
        if len(line.split()) != int(v):
            print("Invalid input file format: Must be a square matrix!")
            exit(1)
    return int(v)


def readFile():
    m = []
    f = open(sys.argv[2], "r")
    vertex = checkFile(f)
    f.seek(2)
    for line in iter(f):
        m.append(line.split())
    print("## Floyd-Warshall algorithm demonstration ##")
    print("\nNumber of vertices: %d" % vertex)
    print("\nMatrix Size: %dx%d" % (len(m), len(m)))
    for i in range(0, vertex):
        for j in range(0, vertex):
            if m[i][j] == "INF" or m[i][j] == "inf":
                m[i][j] = float("inf")
            else:
                m[i][j] = int(m[i][j])
            print(m[i][j], end=" ")
        print()

    FloydWarshall(m, vertex)
    f.close()


if __name__ == "__main__":
    os.system("clear")
    parser = argparse.ArgumentParser(
        description=
        "Floyd-Warshall algorithm demonstration: use a formatted input file with a number N in the first line, \
  followed by a NxN values that indicate the weights associated with the edges that connect two vertices."
    )
    parser.add_argument(
        "-f",
        metavar="file",
        type=str,
        default=30,
        help="Input file name (e.g. -f input.txt)",
        required=True,
    )
    args = parser.parse_args()

    readFile()
