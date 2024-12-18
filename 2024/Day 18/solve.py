# Advent of Code Day 18

from collections import deque


GRID_W = 71
GRID_H = 71
ROUNDS = 1024
grid = [['.' for i in range(GRID_H)] for j in range(GRID_W)]

bt = open('input.txt', 'r').read().splitlines()
for i in range(ROUNDS):
    x, y = bt[i].split(',')
    x, y = int(x), int(y)
    grid[y][x] = '#'

# bfs, part 1
def is_within_bounds(GRID_W, GRID_H, nx, ny):
    return 0 <= nx < GRID_W and 0 <= ny < GRID_H

def get_pyth_distancen_to_end(x, y):
    return abs(GRID_W - 1 - x) + abs(GRID_H - 1 - y)

q = deque([(0, 0, set())])
gvisited = set()
while q:
    x, y, visited = q.popleft()
    if (x, y) in gvisited:
        continue
    gvisited.add((x, y))

    if x == GRID_W - 1 and y == GRID_H - 1:
        print('Part 1:', len(visited))
        break
    
    
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if is_within_bounds(GRID_W, GRID_H, nx, ny) and (nx, ny) not in visited and grid[ny][nx] == '.':
            new_visited = visited | {(nx, ny)}
            q.append((nx, ny, new_visited))

# part2
grid2 = [['.' for i in range(GRID_H)] for j in range(GRID_W)]

for i2 in range(len(bt)):
    gx, gy = bt[i2].split(',')
    gx, gy = int(gx), int(gy)
    grid2[gy][gx] = '#'
    
    q2 = deque([(0, 0, set())])
    gvisited2 = set()
    found_end = False
    while q2:
        x2, y2, visited = q2.popleft()
        if (x2, y2) in gvisited2:
            continue
        gvisited2.add((x2, y2))

        if x2 == GRID_W - 1 and y2 == GRID_H - 1:
            found_end = True
            break
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x2 + dx, y2 + dy
            if is_within_bounds(GRID_W, GRID_H, nx, ny) and (nx, ny) not in visited and grid2[ny][nx] == '.':
                new_visited = visited | {(nx, ny)}
                q2.append((nx, ny, new_visited))
    
    if not found_end:
        print('Part 2:', f'{gx},{gy}')
        break