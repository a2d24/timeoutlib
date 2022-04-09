

import time

import pytest

import timeoutlib

EPSILON = 1e-2


def test_cannot_set_default_and_default_factory(sleeper_max_2s):
    with pytest.raises(ValueError) as exec_info:
        timeoutlib.timeout(max_duration=1, default=1, default_factory=list)

    assert exec_info.value.args[0] == 'Cannot have both default_factory and default specified'


def test_cannot_default_behaviour_with_custom_exception(sleeper_max_2s):
    expected = 'Cannot have a default return value or factory in combination with an exception to raise'
    with pytest.raises(ValueError) as exec_info:
        timeoutlib.timeout(max_duration=1, default_factory=list, exception=RuntimeError)

    assert exec_info.value.args[0] == expected

    with pytest.raises(ValueError) as exec_info:
        timeoutlib.timeout(max_duration=1, default=list, exception=RuntimeError)

    assert exec_info.value.args[0] == expected


def test_defaults_to_timeoutlibs_exception(sleeper_max_2s):
    sleeper = timeoutlib.timeout(max_duration=1)(lambda duration: time.sleep(duration))
    with pytest.raises(timeoutlib.OperationTimedOut):
        sleeper(2)
