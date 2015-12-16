i = 0
floor = 0

while i == 0:
    print "You are on floor " + str(floor) + ". Type ( to go up or ) to go down. Type done to finish."
    chooseFloor = raw_input()
    if chooseFloor == '(':
        floor += 1
    elif chooseFloor == ')':
        floor -= 1
    elif chooseFloor == 'done' or chooseFloor == 'Done':
        i += 1
    else:
        print "That is invalid syntax"
