i = 0
level = 0

with open('Day1Input.txt') as file:
        for line in file:
            for character in line:
                if character == '(':
                    level += 1
                elif character == ')':
                    level -= 1
print level
