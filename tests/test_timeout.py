import time

import timeoutlib

EPSILON = 1e-2


def test_aborts_in_two_seconds(sleeper_max_2s):
    start = time.perf_counter()
    try:
        assert sleeper_max_2s(3)
    except timeoutlib.OperationTimedOut:
        ...

    end = time.perf_counter()

    assert abs(end - start - 2) < EPSILON


def test_does_not_abort_if_time_not_exceeded(sleeper_max_2s):
    start = time.perf_counter()
    assert sleeper_max_2s(1.9)
    end = time.perf_counter()

    assert abs(end - start - 1.9) < EPSILON