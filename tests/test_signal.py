import signal


def test_does_not_overwrite_default_sigalrm_handler(sleeper_max_2s):
    assert signal.getsignal(signal.SIGALRM) == signal.Handlers.SIG_DFL

    sleeper_max_2s(0.1)

    assert signal.getsignal(signal.SIGALRM) == signal.Handlers.SIG_DFL
