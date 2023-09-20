def warshalls(c, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = c[i][j] or (c[i][k] and c[k][j])

    print("The transitive closure of the graph:")
    for i in range(n):
        for j in range(n):
            print(c[i][j], end=" ")
        print()


def main():
    n = int(input("Enter the number of vertices: "))
    c = []
    print("Enter the adjacency cost matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        c.append(row)

    warshalls(c, n)


main()
