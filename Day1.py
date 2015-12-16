i = 0
level = 0

while i == 0:
    print "You are on floor " + str(level) + "."
    chooseFloor = raw_input()
    if chooseFloor == 'Done' or 'done':
        i += 1
    else:
        for character in chooseFloor:
            if character == '(':
                level += 1
            elif character == ")":
                level -= 1
