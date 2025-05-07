from src.words_frequency import words_frequency


def test_words_frequency_example():
    sentence = "bar baz foo foo zblah zblah zblah baz toto bar"
    n = 3
    expected_output = [("zblah", 3), ("bar", 2), ("baz", 2)]
    assert words_frequency(sentence, n) == expected_output


def test_words_frequency_tie_breaker():
    sentence = "bar baz foo foo zblah zblah"
    n = 2
    expected_output = [("foo", 2), ("zblah", 2)]
    assert words_frequency(sentence, n) == expected_output


def test_words_frequency_single_word():
    sentence = "foo"
    n = 1
    expected_output = [("foo", 1)]
    assert words_frequency(sentence, n) == expected_output


def test_words_frequency_empty_sentence():
    sentence = ""
    n = 3
    expected_output = []
    assert words_frequency(sentence, n) == expected_output


def test_words_frequency_more_n_than_words():
    sentence = "baz foo zblah"
    n = 5
    expected_output = [("baz", 1), ("foo", 1), ("zblah", 1)]
    assert words_frequency(sentence, n) == expected_output


def test_words_frequency_with_punctuation():
    sentence = "foo, bar! baz? foo..."
    n = 2
    expected_output = [("foo", 2), ("bar", 1)]
    assert words_frequency(sentence, n) == expected_output


def test_words_frequency_case_sensitivity():
    sentence = "Foo foo FOO bar Bar BaR"
    n = 2
    expected_output = [("bar", 3), ("foo", 3)]
    assert words_frequency(sentence, n) == expected_output


def test_words_frequency_zero_n():
    sentence = "foo bar baz"
    n = 0
    expected_output = []
    assert words_frequency(sentence, n) == expected_output


def test_words_frequency_negative_n():
    sentence = "foo bar baz"
    n = -15
    try:
        words_frequency(sentence, n)
        assert False, "Expected ValueError for negative n"
    except ValueError as e:
        assert str(e) == "n must be greater than or equal to zero."
