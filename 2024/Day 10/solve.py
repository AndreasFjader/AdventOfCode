# Advent of Code Day 10
from collections import deque

def get_starting_coords(input: list[list[int]]) -> list[tuple[int, int]]:
    return [(x, y) for y in range(len(input)) for x in range(len(input[y])) if input[y][x] == 0]

def parse_grid(input: list[str]) -> list[list[int]]:
    return [[int(c) for c in row] for row in input]

def neighbor_offsets():
    return [(0, 1), (0, -1), (1, 0), (-1, 0)]

def is_outside_grid(grid, nx, ny):
    return nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid)

def is_valid_neighbor(grid, x, y, nx, ny):
    return grid[ny][nx] == grid[y][x] + 1

def find_trails(input: list[str], find_all_trails: bool) -> int:
    grid = parse_grid(input)
    
    scores = []
    for x, y in get_starting_coords(grid):
        # Do a BFS to find how many 9:s are reachable from the starting coord.
        q = deque([(x, y)])
        score = 0
        found_nines = set()
        while q:
            x, y = q.popleft()

            if grid[y][x] == 9:
                if find_all_trails:
                    score += 1
                elif (x, y) not in found_nines:
                    score += 1
                    found_nines.add((x, y))
                continue
            
            for dy, dx in neighbor_offsets():
                nx, ny = x + dx, y + dy
                
                # Ignore coords that are out of bounds
                if is_outside_grid(grid, nx, ny):
                    continue

                if is_valid_neighbor(grid, x, y, nx, ny):
                    q.append((nx, ny))

        scores.append(score)

    return sum(scores)

def part1(input: list[str]) -> int:
    return find_trails(input, False)

def part2(input: list[str]) -> int:
    return find_trails(input, True)

if __name__ == '__main__':
    test_input = open('test.txt').read().splitlines()
    actaul_input = open('input.txt').read().splitlines()

    print('Part 1 (test):', part1(test_input))
    print('Part 1 (actual):', part1(actaul_input))
    print('Part 2 (test):', part2(test_input))
    print('Part 2 (actual):', part2(actaul_input))