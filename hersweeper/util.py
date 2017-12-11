def to_number(letters):
    if not letters:
        raise ValueError("a letter is needed")

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    result = -1
    for pos, letter in enumerate(letters):
        try:
            index = alphabet.index(letter)
            result += (index + 1) * 26**(len(letters) - pos - 1)
        except ValueError:
            raise ValueError(f"'{letter}' is not a valid character")

    return result
