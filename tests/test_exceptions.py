import pytest

import timeoutlib

EPSILON = 1e-2


def test_raises_default_exception(sleeper_max_2s):
    assert sleeper_max_2s(0.1)

    with pytest.raises(timeoutlib.OperationTimedOut):
        assert sleeper_max_2s(3)


def test_caught_by_builtin_timeouterror(sleeper_max_2s):
    assert sleeper_max_2s(0.1)

    with pytest.raises(TimeoutError):
        assert sleeper_max_2s(3)


def test_raises_custom_class_exception(sleeper_max_2s_custom_exception_from_class):
    assert sleeper_max_2s_custom_exception_from_class(0.1)

    with pytest.raises(ValueError):
        assert sleeper_max_2s_custom_exception_from_class(3)


def test_raises_custom_instance_exception(sleeper_max_2s_custom_exception_from_instance):
    assert sleeper_max_2s_custom_exception_from_instance(0.1)

    with pytest.raises(ValueError) as exc_info:
        assert sleeper_max_2s_custom_exception_from_instance(3)

    assert exc_info.value.args[0] == "Bad value"