# Advent of Code Day 4
WORDS = {'XMAS', 'SAMX'}
APPLICABLE_X_WORDS = {'MMASS', 'SSAMM', 'SMAMS', 'MSASM'}
ALL_COORD_OFFSETS = {
    ((0, 0), (1, 0), (2, 0), (3, 0)), # vertical forward
    ((-3, 0), (-2, 0), (-1, 0), (0, 0)), # vertical backwards
    ((0, -3), (0, -2), (0, -1), (0, 0)), # horizontal upward
    ((0, 0), (0, 1), (0, 2), (0, 3)), # horizontal downward
    ((0, 0), (1, -1), (2, -2), (3, -3)), # diagonal up-right
    ((0, 0), (-1, -1), (-2, -2), (-3, -3)), # diagonal up-left
    ((3, 3), (2, 2), (1, 1), (0, 0)), # diagonal down-right
    ((-3, 3), (-2, 2), (-1, 1), (0, 0)) # diagonal down-left
}

# methods for both parts
def is_within_bounds(x: int, y: int, GRID_L: int, GRID_H: int) -> bool:
    return x >= 0 and x < GRID_L and y >= 0 and y < GRID_H

def find_word(grid: list[list], coords: tuple[tuple]) -> str:
    return "".join([grid[y][x] for x, y in coords])

def are_cords_within_bounds(coords: tuple, GRID_H: int, GRID_L: int) -> bool:
    return all([is_within_bounds(x, y, GRID_L, GRID_H) for x, y in coords])

# Method for part 2
def check_mas(x, y, GRID_H, GRID_L, inp, seen) -> int:
    letter = inp[y][x]    
    if letter == 'A':
        # It's in the middle
        coords = ((x-1, y-1), (x - 1, y + 1), (x, y), (x + 1, y + 1), (x + 1, y - 1))
        if not are_cords_within_bounds(coords, GRID_H, GRID_L) or coords in seen:
            return 0

        xword = "".join([inp[y][x] for x, y in coords])
        if xword in APPLICABLE_X_WORDS:
            seen.add(coords)
            return 1

    return 0

# Part 1
def part1(grid: list[str]) -> int:
    GRID_H, GRID_L = len(grid), len(grid[0])
    seen = set()
    matches = 0
    for y in range(GRID_H):
        for x in range(GRID_L):
            for coord_offsets in ALL_COORD_OFFSETS:
                coords = tuple((x+dx, y+dy) for dx, dy in coord_offsets)
                if coords in seen or not are_cords_within_bounds(coords, GRID_H, GRID_L):
                    continue
                
                if find_word(grid, coords) in WORDS:
                    seen.add(coords)
                    matches += 1
    return matches

# Part 2
def part2(grid: list[str]) -> int:
    GRID_H, GRID_L = len(grid), len(grid[0])
    seen = set()
    return sum([check_mas(x, y, GRID_H, GRID_L, grid, seen) for y in range(GRID_H) for x in range(GRID_L)])

if __name__ == '__main__':
    test_input = open('test.txt', 'r').read().splitlines()
    actual_input = open('input.txt', 'r').read().splitlines()

    # Part 1
    print('Part 1 (test):', part1(test_input)) # 18
    print('Part 1 (actual):', part1(actual_input)) # 2401

    # Part 2
    print('Part 2 (test):', part2(test_input)) # 9
    print('Part 2 (actual):', part2(actual_input)) # 1822
