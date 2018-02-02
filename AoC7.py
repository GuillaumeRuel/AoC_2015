d = {'AND': '&', 'OR': '|', 'LSHIFT': '<<', 'RSHIFT': '>>', 'NOT': '~'}
value = {}
evaluator = []
with open('data/day7.txt', 'r') as puzzle:
    puzzle = puzzle.readlines()
    for line in puzzle:
        line = line.replace('\n', '')
        var = line.split(' -> ')[1]
        val = line.split(' -> ')[0]
        curr = val.split()
        flag = True

        for i in xrange(len(curr)):
            try:
                d[curr[i]]
            except KeyError:
                if curr[i].isdigit() and not any([x in d or x in d.values() for x in curr]):
                    value[var] = curr[i]
                    break
        evaluator.append([var, ' '.join(curr)])

    for items in evaluator:
        ans = ""
        flag = True
        for x in items[1].split():
            if x in value.keys():
                #part 2
                if x == 'b':
                    ans += '16076'
                else:
                    ans += str(value[x])
            elif x in d.keys():
                ans += d[x]
            else:
                ans += x
            
        try:
            value[items[0]] = eval(ans)%65536
        except:
            evaluator.append(items)
    
    print value['a']
