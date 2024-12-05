# Advent of Code Day 5

def create_ordering_map(ordering: str) -> dict:
    ordering_map = {}
    for line in ordering.split('\n'):
        i, j = line.split('|')
        i, j = int(i), int(j)
        if i not in ordering_map:
            ordering_map[i] = []
        ordering_map[i].append(j)
        
    return ordering_map

def create_update_sequence(update_sequence: str) -> list:
    return [list(map(int, x.split(','))) for x in update_sequence.split('\n')]

def is_valid_sequence(sequence: list[int], ordering: dict) -> bool:
    for i in range(len(sequence) - 1):
        first, rest = sequence[i], sequence[i+1:]
        if first not in ordering:
            return False
        
        if not all([n in ordering[first] for n in rest]):
            return False
    
    return True

# Part 2
def correct_sequence(sequence: list[int], ordering: dict) -> list[int]:
    temp_sequence = sequence.copy()
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            t1, t2 = temp_sequence[i], temp_sequence[i+1:]
            if t1 in ordering and all([n in ordering[t1] for n in t2]):
                continue

            # Swap elements.
            temp_sequence[i], temp_sequence[j] = temp_sequence[j], temp_sequence[i]
        if is_valid_sequence(temp_sequence, ordering):
            return temp_sequence[len(temp_sequence) // 2]

    raise ValueError('No valid sequence found.')

# Solutions
def part1(sequences: str, ordering: str) -> int:
    mapped_ordering = create_ordering_map(ordering)
    update_sequence = create_update_sequence(sequences)

    return sum([s[len(s) // 2] for s in update_sequence if is_valid_sequence(s, mapped_ordering)])

def part2(sequences: str, ordering) -> int:
    mapped_ordering = create_ordering_map(ordering)
    update_sequence = create_update_sequence(sequences)

    invalid_sequences = [s for s in update_sequence if not is_valid_sequence(s, mapped_ordering)]
    return sum([correct_sequence(invsq, mapped_ordering) for invsq in invalid_sequences])

if __name__ == '__main__':
    test_ordering, test_sequences = open('test.txt', 'r').read().split('\n\n')
    actual_ordering, actual_sequences = open('input.txt', 'r').read().split('\n\n')

    print('Part 1 (test):', part1(test_sequences, test_ordering))
    print('Part 1 (actual):', part1(actual_sequences, actual_ordering))

    print('Part 2 (test):', part2(test_sequences, test_ordering))
    print('Part 2 (actual):', part2(actual_sequences, actual_ordering))
