import time

import pytest

import timeoutlib


def test_bad_default_values(sleeper_max_2s):
    with pytest.raises(AssertionError):
        sleeper = timeoutlib.timeout(max_duration=-1)(lambda duration: time.sleep(duration))

    with pytest.raises(AssertionError):
        sleeper = timeoutlib.timeout(max_duration=0)(lambda duration: time.sleep(duration))

