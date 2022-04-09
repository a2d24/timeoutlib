import time

import pytest

import timeoutlib


def sleeper(duration):
    time.sleep(duration)
    return True


@pytest.fixture
def sleeper_max_2s_default_value():
    yield timeoutlib.timeout(max_duration=2, default=False)(sleeper)


@pytest.fixture
def sleeper_max_2s_default_factory():
    yield timeoutlib.timeout(max_duration=2, default_factory=list)(sleeper)


@pytest.fixture
def sleeper_max_2s():
    yield timeoutlib.timeout(max_duration=2)(sleeper)

@pytest.fixture
def sleeper_mutable_default_list():
    yield timeoutlib.timeout(max_duration=2, default=[])(sleeper)


@pytest.fixture
def sleeper_max_2s_custom_exception_from_class():
    yield timeoutlib.timeout(max_duration=2, exception=ValueError)(sleeper)

@pytest.fixture
def sleeper_max_2s_custom_exception_from_instance():
    yield timeoutlib.timeout(max_duration=2, exception=ValueError("Bad value"))(sleeper)
