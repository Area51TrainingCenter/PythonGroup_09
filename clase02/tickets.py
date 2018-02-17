def ticket_check(section, seats):
    if section == 'F':
        return seats <= 4
    elif section == 'G':
        return seats <= 10
    else:
        return False


section = input('Choose a section general or floor: ')
seats = int(input('Choose a seat between 1 - 10: '))

valid = ticket_check(section, seats)
if valid:
    print('Valid ticket')
else:
    print('Not valid')
