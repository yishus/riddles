import itertools

def solution(times, times_limit):
    bunnies = len(times) - 2
    shortest = floyd_warshall(times)
    # negative cycle
    for i in range(len(shortest)):
        if shortest[i][i] < 0:
            return range(bunnies)
    for k in range(bunnies + 1, 1, -1):
        for perm in itertools.permutations(range(1, bunnies + 1), k):
            paths = edges(perm)
            total_cost = 0
            for x, y in paths:
                total_cost += shortest[x][y]
            if total_cost <= times_limit:
                return sorted(list(i - 1 for i in perm))


def edges(vertices):
    nodes = [0] + list(vertices) + [-1]
    paths = []
    for i in range(len(nodes) - 1):
        paths.append((nodes[i], nodes[i + 1]))

    return paths


def floyd_warshall(G):
    nV = len(G)
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance