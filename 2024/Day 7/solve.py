# Advent of Code Day 7

def calc_result(equation: list[str]) -> int:
    res = int(equation[0])
    for i in range(1, len(equation), 2):
        if equation[i] == '+':
            res += int(equation[i + 1])
        elif equation[i] == '*':
            res *= int(equation[i + 1])
        elif equation[i] == '||':
            res = int(str(res) + str(equation[i + 1]))
    
    return res

def is_valid_equation(numbers: list[str], result: int, operators: list[str], index: int = 1) -> bool:
    if index >= len(numbers):
        return calc_result(numbers) == result
    
    for operator in operators:
        new_numbers = numbers[:index] + [operator] + numbers[index:]
        if is_valid_equation(new_numbers, result, operators, index + 2):
            return True

    return False

def solve_with_operands(lines: list[str], operators: list[str]) -> int:
    return sum([
        int(result) for result, equation in [line.split(': ') for line in lines] 
        if is_valid_equation(equation.split(' '), int(result), operators)
    ])

if __name__ == '__main__':
    test_input = open('test.txt', 'r').read().splitlines()
    actual_input = open('input.txt', 'r').read().splitlines()

    operands_p1 = ['+', '*']
    operands_p2 = ['+', '*', '||']

    print('Part 1 (test):', solve_with_operands(test_input, operands_p1))
    print('Part 1 (actual):', solve_with_operands(actual_input, operands_p1))
    print('Part 2 (test):', solve_with_operands(test_input, operands_p2))
    print('Part 2 (actual):', solve_with_operands(actual_input, operands_p2))