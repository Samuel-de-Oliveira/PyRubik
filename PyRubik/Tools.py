__all__: list = ['reverse', 'is_wca_notation']


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


def is_wca_notation(scramble: list) -> bool:
    """
    Function that verify if a list is a official WCA notation.
    Usefull if someone digit a wrong notation on a input box, for
    example.
    """
    # Tuples with the valid notation for moves
    valid_notation_cubes: tuple = ('U', 'D', 'R', 'L', 'F', 'B')
    valid_notation_clock: tuple = ()
    valid_notation_megaminx: tuple = ()

    # TODO: Finish this part of code in next version

    return True


if __name__ == '__main__':
    print(
        'This is a module file, then you should import it.\n'
        + 'Plase, take a look in https://github.com/Samuel-de-Oliveira/PyRubik for more info'
    )
