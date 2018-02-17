import string
import age20
from rainbow import rainbow_color
# from matematicas.constantes import PI


def rainbow_or_age(chamuyo):
    if chamuyo in string.ascii_letters:
        return rainbow_color(chamuyo)
    else:
        return age20.age_20(int(chamuyo))


if __name__ == '__main__':
    valor = input('Ingrese una letra o un número: ')
    print(rainbow_or_age(valor))
