class AoC6:

    puzzle = ''
    grid = {}

    def __init__(self):
        self.puzzle = open('data\day6.txt').read().split('\n')
        for y in xrange(1000):
            for x in range(1000):
                self.grid[(x,y)] = 0
    
        self.solve()
    
    def turn_on(self, xi, yi, xf, yf):
        for y in xrange(yi, yf + 1):
            for x in xrange(xi, xf + 1):
                t = (x, y)
                self.grid[t] += 1

    def turn_off(self, xi, yi, xf, yf):
        for y in xrange(yi, yf + 1):
            for x in xrange(xi, xf + 1):
                t = (x, y)
                if self.grid[t] > 0:
                    self.grid[t] -= 1

    def toggle(self, xi, yi, xf, yf):
        for y in xrange(yi, yf + 1):
            for x in xrange(xi, xf + 1):
                t = (x, y)
                self.grid[t] += 2

    def solve(self):    
        for line in self.puzzle:
            line = line.split() 

            if line[0] == 'turn' and line[1] == 'on':
                i = map(int, line[2].split(','))
                f = map(int, line[4].split(','))
                self.turn_on(i[0], i[1], f[0], f[1])

            elif line[0] == 'turn' and line[1] == 'off':
                i = map(int, line[2].split(','))
                f = map(int, line[4].split(','))
                self.turn_off(i[0], i[1], f[0], f[1])

            elif line[0] == 'toggle':
                i = map(int, line[1].split(','))
                f = map(int, line[3].split(','))
                self.toggle(i[0], i[1], f[0], f[1])

        print(sum([int(v) for k,v in self.grid.items()]))

if __name__ == '__main__':
    a = AoC6()