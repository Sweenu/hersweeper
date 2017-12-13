from hersweeper.cli import *

test_game = CommandLine()


class TestCommandLine:
    def test__process_input_success(self):
        test_samples = [('a8', (0, 7)),
                        ('58jh', (267, 57)),
                        ('zzz397', (18277, 396))]
        for sample in test_samples:
            assert test_game._process_input(sample[0]) == sample[1]
