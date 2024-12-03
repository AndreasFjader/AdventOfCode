# Advent of Code Day 3

import re

def calc_sum(matches):
    mult_sum = []
    for match in matches:
        rem = match.replace('mul(', '').replace(')', '').split(',')
        mult_sum.append(int(rem[0]) * int(rem[1]))
    return sum(mult_sum)

def read_input_from(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()

def find_matches(re_pattern: str, lines: list[str]) -> list[str]:
    matches = []
    for line in lines:
        matches.extend(re.findall(re_pattern, line))
    return matches

def filter_out_donts(matches: list[str]) -> list[str]:
    mul_after_dont = []
    is_dont = False
    for match in matches:
        if match == 'do()':
            is_dont = False
        elif match == "don't()":
            is_dont = True
        elif 'mul' in match and not is_dont:
            mul_after_dont.append(match)
    return mul_after_dont

def part1(input: list[str]) -> int:
    re_pattern = r'mul\(\d+,\d+\)'
    mul_matches = find_matches(re_pattern, input)
    
    return calc_sum(mul_matches)

def part2(input: list[str]) -> int:
    re_patterns_2 = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    mul_matches = find_matches(re_patterns_2, input)
    return calc_sum(filter_out_donts(mul_matches))

if __name__ == '__main__':
    test1 = ['xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))']
    test2 = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    
    input = read_input_from('input.txt')
    
    print('Part 1 (test):', part1(test1))
    print('Part 1 (input):', part1(input))
    print('Part 2 (test):', part2(test2))
    print('Part 2 (input):', part2(input))
