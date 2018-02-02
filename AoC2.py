##part 1
paper = 0
with open('data/day2.txt', 'r')as puzzle:
    for line in puzzle:
        line = map(int ,line.replace('\n','').split('x'))
        dim = [line[0] * line [1], line[1] * line[2], line[2] * line[0]]
        paper += 2 * sum(dim) + min(dim)

print paper 

##part 2
ribon = 0
with open('data/day2.txt', 'r')as puzzle:
    for line in puzzle:
        line = sorted(map(int ,line.replace('\n','').split('x')))
        ribon += line[0] * 2 + line[1] * 2 + reduce((lambda x, y: x*y), line)
print ribon 