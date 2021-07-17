import collections

def solution(map):
    height = len(map)
    width = len(map[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = collections.deque([])
    # row, col, steps, remaining wall to remove
    q.append((0, 0, 1, 1))
    seen = set([(0, 0)])

    while q:
        r, c, steps, k = q.popleft()
        if r == width - 1 and c == height - 1:
            return steps
        else:
            for x, y in directions:
                nr = r + x
                nc = c + y
                if nr < width and nr >= 0 and nc < height and nc >= 0 and (nr, nc) not in seen:
                    if map[nc][nr] == 1:
                        if k > 0:
                            seen.add((nr, nc))
                            q.append((nr, nc, steps + 1, k-1))
                    else:
                        seen.add((nr, nc))
                        q.append((nr, nc, steps + 1, k))

    return -1