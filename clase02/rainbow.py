# print the color matching the letter
# R = Red
# O = Orange
# Y = Yellow
# G = Green
# B = Blue
# I = Indigo
# V = Violet
# else print "no match"


#   rainbow_color('R')
def rainbow_color(color):
    color_lower = color.upper()
    colors = {
        'R': 'Red',
        'O': 'Orange',
        'Y': 'Yellow',
        'G': 'Green',
        'B': 'Blue',
        'I': 'Indigo',
        'V': 'Violet',
    }

    if color_lower in colors:
        return colors[color_lower]
    else:
        return 'No match'


if __name__ == '__main__':
    color = input('Ingrese una letra de un color de arcoiris: ')
    print(rainbow_color(color))
