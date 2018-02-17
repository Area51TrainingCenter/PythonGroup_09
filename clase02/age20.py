age = 20


def age_20(age):
    if age == 20:
        return 'Tienes 20'
    else:
        return 'Tienes {} años {} de 20'.format(
            age - 20 if age > 20 else 20 - age,
            'más' if age > 20 else 'menos'
        )

    # elif age > 20:
    #     return 'Tienes {} años más de 20'.format(age - 20)
    # else:
    #     return 'Tienes {} años menos de 20'.format(20 - age)


# edad = int(input('Cuántos años tienes? '))
# print(age_20(edad))
