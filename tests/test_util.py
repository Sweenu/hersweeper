import pytest

from hersweeper.util import to_number


def test_to_number_success():
    test_samples = {('a', 0), ('y', 24), ('aa', 26), ('oui', 10694)}
    for sample in test_samples:
        assert to_number(sample[0]) == sample[1]


def test_to_number_fail():
    with pytest.raises(ValueError) as e:
        to_number('mon$ieur')
    assert e.value.args[0] == "'$' is not a valid character"

    with pytest.raises(ValueError) as e:
        to_number('')
    assert e.value.args[0] == 'a letter is needed'
