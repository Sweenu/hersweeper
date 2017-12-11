import pytest

from hersweeper.util import to_number


def test_to_number_success():
    test_samples = {('y', 25), ('aa', 27), ('oui', 10695)}
    for sample in test_samples:
        assert to_number(sample[0]) == sample[1]


def test_to_number_fail():
    with pytest.raises(ValueError) as e:
        to_number('mon$ieur')
    assert e.value.args[0] == "'$' is not a valid character"

    with pytest.raises(ValueError) as e:
        to_number('')
    assert e.value.args[0] == 'a letter is needed'
