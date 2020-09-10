import string


def startswith_capital_counter(names):
    count = 0
    for name in names:
        if name[0] in string.ascii_uppercase:
            count += 1
    return count
