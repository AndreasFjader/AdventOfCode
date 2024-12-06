# Advent of Code 6

def parse_input(grid: list[str], add_obstacle: tuple = None):
    # Should return:
    #  - set with positions of obstacles
    #  - tuple with guards starting position
    
    GRID_H = len(grid)
    GRID_W = len(grid[0])
    guard_pos = None
    obstacles = set()
    for r in range(GRID_H):
        for c in range(GRID_W):
            if grid[r][c] == '#':
                obstacles.add((r, c))
            elif grid[r][c] == '^':
                guard_pos = (r, c)
    
    if add_obstacle:
        obstacles.add(add_obstacle)
    return obstacles, guard_pos, GRID_H, GRID_W

def get_next_pos_and_direction(obstacles: set, guard_pos: tuple, direction: int):
    # directions: 0 = up, 1 = right, 2 = down, 3 = left
    direction_offset = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

    # Check if there is an obstacle in the current direction's next step
    new_pos = None
    while not new_pos:
        check_new_pos = (guard_pos[0] + direction_offset[direction][0], guard_pos[1] + direction_offset[direction][1])
        if check_new_pos in obstacles:
            # Turn right
            direction = (direction + 1) % 4
        else:
            new_pos = check_new_pos
            break
    
    return new_pos, direction

def is_within_grid(pos: tuple, GRID_H: int, GRID_W: int):
    return 0 <= pos[0] < GRID_H and 0 <= pos[1] < GRID_W

def part1(grid: list[str]) -> int:
    obstacles, guard_pos, GRID_H, GRID_W = parse_input(grid)
    visited = set()

    direction = 0
    while is_within_grid(guard_pos, GRID_H, GRID_W):
        visited.add(guard_pos)
        guard_pos, direction = get_next_pos_and_direction(obstacles, guard_pos, direction)
    
    return len(visited)

def part2(grid: list[str]) -> int:
    # Add a single obstacle at a location where there isn't any, to see if the guard ends up in a loop.
    # How to decide when the guard is in a loop? If the guard has visited the same position, with the same direction, it's a loop.
    GRID_H = len(grid)
    GRID_W = len(grid[0])
    different_positions = 0
    for r in range(GRID_H):
        for c in range(GRID_W):
            obstacles, guard_pos, _, _ = parse_input(grid, (r, c))

            visited = set()
            direction = 0
            cont = True
            while is_within_grid(guard_pos, GRID_H, GRID_W) and cont:
                visited.add((guard_pos, direction))
                guard_pos, direction = get_next_pos_and_direction(obstacles, guard_pos, direction)

                if (guard_pos, direction) in visited:
                    cont = False
                    different_positions += 1
    
    return different_positions

if __name__ == '__main__':
    test_input = open('test.txt', 'r').read().splitlines()
    actual_input = open('input.txt', 'r').read().splitlines()

    print('Part 1 (test):', part1(test_input))
    print('Part 1 (actual):', part1(actual_input))

    print('Part 2 (test):', part2(test_input))
    print('Part 2 (actual):', part2(actual_input))