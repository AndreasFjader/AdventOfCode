# Advent of Code Day 15

def parse_input(input: str):
    grid, directions = input.split('\n\n')
    grid = [list(g) for g in grid.splitlines()]
    guard = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                guard = (x, y)
                break

    return (grid, guard, "".join(directions.splitlines()))

def is_within_grid(grid: list[str], x: int, y: int) -> bool:
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def get_gps_score(grid: list[str]):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                count += (100 * y + x)
    
    return count

def get_boxes_in_line(grid, x, y, dx, dy):
    boxes = []
    nx, ny = x, y
    found_free_space = False
    while grid[ny][nx] != '#':
        nx += dx
        ny += dy

        if not is_within_grid(grid, nx, ny):
            break

        if grid[ny][nx] == '.':
            found_free_space = True
            boxes.append((nx, ny))
            break

        if grid[ny][nx] == 'O':
            boxes.append((nx, ny))
    
    return boxes if found_free_space else []


def part1(puzzle_input: str) -> int:
    grid, guard, directions = parse_input(puzzle_input)
    for d in directions:
        (x, y) = guard
        dx = 1 if d == '>' else -1 if d == '<' else 0
        dy = 1 if d == 'v' else -1 if d == '^' else 0
        # print(dx, dy)
        
        if not is_within_grid(grid, x+dx, y+dy) or grid[y+dy][x+dx] == '#':
            continue

        if grid[y+dy][x+dx] == '.':
            grid[y][x] = '.'
            grid[y+dy][x+dx] = '@'
            guard = (x+dx, y+dy)
            # print_grid(grid)
            continue

        # Else we've hit a box.
        boxes = get_boxes_in_line(grid, x, y, dx, dy)
        # print(boxes)
        if len(boxes) == 0:
            continue

        grid[boxes[0][1]][boxes[0][0]] = '.'
        grid[boxes[-1][1]][boxes[-1][0]] = 'O'

        grid[y][x] = '.'
        grid[y+dy][x+dx] = '@'
        guard = (x+dx, y+dy)
        # print_grid(grid)
        # print('\n')


    return get_gps_score(grid)

def print_grid(grid):
    for col in grid:
        r = []
        for c in col:
            r.append(c)
        print("".join(r))


if __name__ == "__main__":
    # Part 1
    test_input = open('test.txt').read()
    actual_input = open('input.txt').read()

    print('Part 1 (test):', part1(test_input))
    print('Part 1 (test):', part1(actual_input))