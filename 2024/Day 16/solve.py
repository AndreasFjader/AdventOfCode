# Advent of Code Day 16

from collections import deque
from heapq import heappush, heappop

def find_start_and_end(maze: list[str]):
    start = end = None
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                start = (x, y)
            elif maze[y][x] == 'E':
                end = (x, y)
    return start, end

def get_turn(direction: int, next_direction: int) -> int:
    return (next_direction - direction + 4) % 4

def calc_new_score(score: int, turn: int) -> int:
    return score + (1001 if turn in (1, 3) else 1)

def part2(maze: list[str]) -> int:
    # Implement a form of backtracking to find the shortest path
    start, end = find_start_and_end(maze)
    
    NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
    queue = []
    
    best_score = float('inf')
    best_score_path = dict()
    backtrack = dict()
    end_states = set()
    
    heappush(queue, (0, start, EAST))
    
    while queue:
        score, (x, y), direction = heappop(queue)
        
        if score > best_score:
            break
        
        if (x, y) == end:
            best_score = score
            end_states.add((x, y, direction))
            
        for dx, dy, next_direction in [(0, 1, SOUTH), (0, -1, NORTH), (1, 0, EAST), (-1, 0, WEST)]:
            nx, ny = x + dx, y + dy
            
            if maze[ny][nx] == '#':
                continue
            
            turn = get_turn(direction, next_direction)
            updated_score = calc_new_score(score, turn)
            
            next_state = (nx, ny, next_direction)
            if updated_score > best_score_path.get(next_state, float('inf')):
                continue
            
            if next_state not in best_score_path or updated_score < best_score_path[next_state]:
                best_score_path[next_state] = updated_score

            if next_state not in backtrack:
                backtrack[next_state] = set()
            backtrack[(nx, ny, next_direction)].add((x, y, direction))
            
            heappush(queue, (updated_score, (nx, ny), next_direction))

    # Backtrack through all the tiles we stepped on.
    q = deque(end_states)
    visited = set(end_states)
    while q:
        k = q.popleft()
        for n in backtrack.get(k, []):
            if n in visited:
                continue
            visited.add(n)
            q.append(n)
    
    unique_tiles = {(x, y) for x, y, _ in visited}
    return len(unique_tiles)

def part1(maze: list[str]) -> int:
    start, end = find_start_and_end(maze)
    
    NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
    queue = []
    heappush(queue, (0, start, EAST, set(start)))
    lowest_score = float('inf')
    
    while queue:
        score, (x, y), direction, visited = heappop(queue)
        
        if score > lowest_score:
            continue
        
        if (x, y) == end:
            return score
            
        for dx, dy, next_direction in [(0, 1, SOUTH), (0, -1, NORTH), (1, 0, EAST), (-1, 0, WEST)]:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= len(maze[0]) or ny < 0 or ny >= len(maze):
                continue
            
            if maze[ny][nx] == '#' or (nx, ny) in visited:
                continue
            
            turn = get_turn(direction, next_direction)
            updated_score = calc_new_score(score, turn)
            visited.add((nx, ny))
            heappush(queue, (updated_score, (nx, ny), next_direction, visited))

if __name__ == '__main__':
    test_input = open('test.txt', 'r').read().splitlines()
    actual_input = open('input.txt', 'r').read().splitlines()
    
    print('Part 1 (test):', part1(test_input))
    print('Part 1 (actual):', part1(actual_input))
    print('Part 2 (test):', part2(test_input))
    print('Part 2 (actual):', part2(actual_input))
