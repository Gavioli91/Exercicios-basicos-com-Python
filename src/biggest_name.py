def find_biggest_name(names: list[str]) -> str:

    char_name = ''
    for name in names:
        if len(name) > len(char_name):
            char_name = name
    return char_name
