file = 'in'
delimiter = '   '

input = open(f'{file}.txt', 'r').read().splitlines()

nrs1 = sorted(int(x.split(delimiter)[0]) for x in input)
nrs2 = sorted(int(x.split(delimiter)[1]) for x in input)

print('Part 1: ', sum([abs(y - x) for x, y in zip(nrs1, nrs2)]))
print('Part 2: ', sum([(x * nrs2.count(x)) for x in nrs1]))