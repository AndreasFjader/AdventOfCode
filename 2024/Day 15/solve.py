# Advent of Code Day 15
from collections import deque

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

def parse_input_2(puzzle_input: str):
    parsed_map = []
    grid, directions = puzzle_input.split('\n\n')
    grid = [list(g) for g in grid.splitlines()]
    for line in grid:
        s = ""
        for c in line:
            if c == '.': s += '..'
            elif c == '#': s += '##'
            elif c == 'O': s += '[]'
            elif c == '@': s += '@.'
        parsed_map.append(list(s))
    
    guard = None
    for y in range(len(parsed_map)):
        for x in range(len(parsed_map[0])):
            if parsed_map[y][x] == '@':
                guard = (x, y)
                break
    
    return (parsed_map, guard, "".join(directions.splitlines()))

def is_within_grid(grid: list[str], x: int, y: int) -> bool:
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def get_gps_score(grid: list[str], c: str) -> int:
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == c:
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
        
        if not is_within_grid(grid, x+dx, y+dy) or grid[y+dy][x+dx] == '#':
            continue

        if grid[y+dy][x+dx] == '.':
            grid[y][x] = '.'
            grid[y+dy][x+dx] = '@'
            guard = (x+dx, y+dy)
            continue

        # Else we've hit a box.
        boxes = get_boxes_in_line(grid, x, y, dx, dy)
        if len(boxes) == 0:
            continue

        grid[boxes[0][1]][boxes[0][0]] = '.'
        grid[boxes[-1][1]][boxes[-1][0]] = 'O'

        grid[y][x] = '.'
        grid[y+dy][x+dx] = '@'
        guard = (x+dx, y+dy)

    return get_gps_score(grid, 'O')

def part2(puzzle_input: str) -> int:
    grid, guard, directions = parse_input_2(puzzle_input)
    for d in directions:
        (x, y) = guard
        dx = 1 if d == '>' else -1 if d == '<' else 0
        dy = 1 if d == 'v' else -1 if d == '^' else 0
        
        nx, ny = x+dx, y+dy
        next_grid_spot = grid[ny][nx]
        if not is_within_grid(grid, nx, ny) or next_grid_spot == '#':
            continue
        
        if next_grid_spot == '.':
            grid[y][x] = '.'
            grid[ny][nx] = '@'
            guard = (nx, ny)
            continue
        
        # Else we've hit [ or ].
        # Moving sideways is similar to part 1
        if dy == 0 and dx != 0:
            simx = nx
            moved_boxes_sim = []
            while True:
                c = grid[ny][simx]
                if c in '[]':
                    moved_boxes_sim.append((simx + dx, ny, c))
                elif c == '#':
                    moved_boxes_sim.clear()
                    break
                elif c == '.':
                    break
                simx += dx
                
            if len(moved_boxes_sim) == 0:
                continue
            
            for bx, by, bc in moved_boxes_sim:
                grid[by][bx] = bc
            grid[ny][nx] = '@'
            grid[y][x] = '.'
            guard = (nx, ny)
                
        elif dy != 0 and dx == 0:
            # Bit tricker, we need to check +-1 in the x direction to find the entire box
            bx, by = nx, ny
            q = deque([(bx, by)])
            moved_boxes_sim = []
            old_box_pos = []
            seen = set()
            while q:
                bx, by = q.popleft()
                if (bx, by) in seen or not is_within_grid(grid, bx, by):
                    continue
                seen.add((bx, by))
                c = grid[by][bx]
                moved_boxes_sim.append((bx, by+dy, c))
                old_box_pos.append((bx, by))
                
                if c == '[':
                    q.append((bx+1, by))
                    nb = grid[by+dy][bx] # Check if there's a box in the delta Y position
                    if nb in '[]':
                        q.append((bx, by+dy))
                    elif nb == '#':
                        moved_boxes_sim.clear()
                        break
                elif c == ']':
                    q.append((bx-1, by))
                    nb = grid[by+dy][bx]
                    if nb in '[]':
                        q.append((bx, by+dy))
                    elif nb == '#':
                        moved_boxes_sim.clear()
                        break

            if len(moved_boxes_sim) == 0:
                continue

            for bx, by in old_box_pos:
                grid[by][bx] = '.'

            for bx, by, bc in moved_boxes_sim:
                grid[by][bx] = bc

            grid[ny][nx] = '@'
            grid[y][x] = '.'
            guard = (nx, ny)
    return get_gps_score(grid, '[')
    
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
    print('Part 1 (actual):', part1(actual_input))
    print('Part 2 (test):', part2(test_input))
    print('Part 2 (actual):', part2(actual_input))
    
    