def test_completes_successfully_without_timeout(sleeper_max_2s_default_value):
    assert sleeper_max_2s_default_value(1) == True


def test_returns_default_when_times_out(sleeper_max_2s_default_value):
    assert sleeper_max_2s_default_value(3) == False