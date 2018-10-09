from cachedgenerator import cachedgenerator


def test_results_are_cached_after_generator_is_exhausted():
    @cachedgenerator
    def a(x):
        yield x

    b = a(4)
    assert list(b) == [4]
    assert list(b) == [4]
    assert list(b) == [4]


def test_multiple_yields():
    @cachedgenerator
    def a():
        yield 1
        yield 2
        yield 3

    b = a()
    assert list(b) == [1, 2, 3]
    assert list(b) == [1, 2, 3]


def test_simultaneous_iteration():
    @cachedgenerator
    def a():
        yield 1
        yield 2
        yield 3

    c = zip(a(), a())

    assert list(c) == [(1, 1), (2, 2), (3, 3)]
