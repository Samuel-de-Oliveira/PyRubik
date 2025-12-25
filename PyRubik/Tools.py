def reverse(scramble: list) -> list:
    """
    Function that rewrite a scramble backwards
    Ex.:
        ["R", "U", "R'", "U", "D'"] -> ["D", "U'", "R", "U'", "R'"]
    """
    backwards_scramble: list = []
    for move in scramble:
        if move[-1] == "'":
            backwards_scramble.insert(0, move.replace("'", ''))
        else:
            backwards_scramble.insert(0, f"{move}'")

    return backwards_scramble


if __name__ == '__main__':
    print(
        'This is a module file, then you should import it.\n'
        + 'Plase, take a look in https://github.com/Samuel-de-Oliveira/PyRubik for more info'
    )
