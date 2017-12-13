alphabet = list('abcdefghijklmnopqrstuvwxyz')


def to_number(letters: str) -> int:
    if not letters:
        raise ValueError("a letter is needed")

    result = -1
    for pos, letter in enumerate(letters):
        try:
            index = alphabet.index(letter)
            result += (index + 1) * 26**(len(letters) - pos - 1)
        except ValueError:
            raise ValueError(f"'{letter}' is not a valid character")

    return result


def to_letters(nb: int) -> str:
    word = [] if nb != 0 else ['a']
    while nb != 0:
        word.insert(0, alphabet[nb % 26])
        nb //= 26

    return ''.join(word)
