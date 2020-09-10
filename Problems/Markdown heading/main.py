def heading(string, level=1):
    word = ''
    if level > 6:
        level = 6
    if level < 1:
        level = 1
    for _ in range(level):
        word = word + '#'
    return word + ' ' + string
