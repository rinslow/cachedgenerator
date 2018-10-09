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

    b = a()
    c = zip(b, b)

    assert list(c) == [(1, 1), (2, 2), (3, 3)]


def test_performance_of_simultaneous_iteration():
    class Stub:
        calls_counter = 0

    @cachedgenerator
    def generator_with_side_effect():
        Stub.calls_counter += 1
        yield Stub.calls_counter

    g = generator_with_side_effect()

    c = zip(g, g)

    assert list(c) == [(1, 1)]
