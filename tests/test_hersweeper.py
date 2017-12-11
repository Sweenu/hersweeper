from hersweeper import hersweeper

test_game = hersweeper.CommandLine()


class TestCommandLine:
    def test__process_input_success(self):
        test_samples = [('a8', (0, 7)), ('58jh', ()), ('zzz397', ())]
        for sample in test_samples:
            assert test_game._process_input(sample[0]) == sample[1]
