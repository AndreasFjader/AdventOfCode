from collections import deque

ITERATIONS = 2000

# Helper functions

def get_next_number(next_nr):
    prune_val = 16777216

    t1 = ((next_nr * 64) ^ next_nr) % prune_val
    t2 = ((t1 // 32) ^ t1) % prune_val
    return ((t2 * 2048) ^ t2) % prune_val

# Solvers

def part1(numbers: list[int]) -> int:
    sum = 0
    for nr in numbers:
        next_nr = nr
        for _ in range(ITERATIONS):
            next_nr = get_next_number(next_nr)
        sum += next_nr
    return sum

def part2(numbers: list[int]) -> int:
    sequences = {}
    for nr in numbers:
        last_digits = deque(maxlen=4)
        next_nr = nr
        sequences_per_buyer = {}
        for x in range(ITERATIONS):
            next_nr = get_next_number(next_nr)

            ld = int(str(next_nr)[-1])
            if len(last_digits) == 4:
                x1, x2, x3, x4 = last_digits
                s1 = x2 - x1
                s2 = x3 - x2
                s3 = x4 - x3
                s4 = ld - x4
                seq = (s1, s2, s3, s4)

                if not seq in sequences:
                    sequences[seq] = 0
                
                if not seq in sequences_per_buyer:
                    sequences[seq] += ld
                
                sequences_per_buyer[seq] = True
                last_digits.popleft() # Remove the first element, as it's now redundant
            last_digits.append(ld)

    return sequences[max(sequences, key=sequences.get)]

if __name__ == '__main__':
    numbers = list(map(int, open('input.txt').read().splitlines()))

    print('Part 1 (actual):', part1(numbers))
    print('Part 2 (actual):', part2(numbers))