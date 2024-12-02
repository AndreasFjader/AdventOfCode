# Advent of Code 2024 Day 2

def read_input(file: str) -> list[str]:
    with open(f'{file}.txt', 'r') as f:
        return f.read().splitlines()

def level_is_safe(diffs: list[int]) -> bool:
    return all(x > 0 and x < 4 for x in diffs) or all(x < 0 and x > -4 for x in diffs)

def create_diffs(levels: list[int]) -> list[int]:
    return [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]

def map_report_to_list_of_ints(reports: list[str]) -> list[int]:
    return [int(x) for report in reports for x in report.split(' ')]

def part1(reports: list[str]) -> int:
    safe_reports = 0
    for report in reports:
        levels = [int(x) for x in report.split(' ')]

        if level_is_safe(create_diffs(levels)):
            safe_reports += 1
    
    return safe_reports

def part2(reports: list[str]) -> int:
    safe_reports = 0
    for report in reports:
        levels = [int(x) for x in report.split(' ')]
        
        # Create a lis of levels without one of the levels
        for skip in range(len(levels)):
            c = levels.copy()
            check_level_minus_one = []
            c.pop(skip)
            for i in range(len(c) - 1):
                check_level_minus_one.append(c[i] - c[i + 1])

            if level_is_safe(check_level_minus_one):
                safe_reports += 1
                break
    
    return safe_reports

if __name__ == '__main__':
    test_data = read_input('test')
    actual_data = read_input('input')
    
    # Part 1
    print('Part 1 (test):', part1(test_data))
    print('Part 1 (actual):', part1(actual_data))
    
    # Part 2
    print('Part 2 (test):', part2(test_data))
    print('Part 2 (actual):', part2(actual_data))