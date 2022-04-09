def test_defaults_are_mutable(sleeper_mutable_default_list):
    assert sleeper_mutable_default_list(0.1)
    response_1 = sleeper_mutable_default_list(3)

    assert response_1 == []
    response_1.extend([1, 2, 3])

    response_2 = sleeper_mutable_default_list(3)

    assert response_2 == [1, 2, 3]


def test_default_factory_not_mutable(sleeper_max_2s_default_factory):
    assert sleeper_max_2s_default_factory(0.1)
    response_1 = sleeper_max_2s_default_factory(3)

    assert response_1 == []
    response_1.extend([1, 2, 3])

    response_2 = sleeper_max_2s_default_factory(3)

    assert response_2 == []
