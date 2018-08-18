from cachedgenerator import cachedgenerator

def test_results_are_cached_after_generator_is_exhausted():
    @cachedgenerator
    def a(x):
        yield x

    b = a(4)
    assert list(b) == [4]
    assert list(b) == [4]
    assert list(b) == [4]
