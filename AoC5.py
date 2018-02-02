#part 1
disalowed = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
nice = []

with open('data/day5.txt', 'r')as puzzle:
    for line in puzzle:
        line = line.rstrip('\r\n')
        if all(c1 + c2 not in disalowed for c1, c2 in zip(line, line[1:])) and sum([line.count(v) for v in vowels]) >= 3 and any(c1 == c2 for c1, c2 in zip(line, line[1:])):
            nice.append(line)

print('part 1',     len(nice))

#part 2
nice = []
with open('data/day5.txt', 'r')as puzzle:
    for line in puzzle:
        line = line.rstrip('\r\n')

        duo = [''.join(x) for x in zip(line, line[1:])]
        filtered = any(duo[i] in duo[i + 2:] for i in xrange(len(duo) - 2))
        same_separated = any(duo[i] == duo[i+1][::-1] for i in xrange(len(duo) - 1))

        if filtered and same_separated:
            nice.append(line)

print('part 2', len(nice))