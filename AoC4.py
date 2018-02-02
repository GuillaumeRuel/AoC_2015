import md5

puzzle = "yzbqklnj"
val = 1

while True:
    m = md5.new(puzzle + str(val))
    #PART 2 6 ZERO
    if str(m.hexdigest()).startswith('000000'):
        print(str(m.hexdigest()))
        print(str(val))
        break
    val += 1