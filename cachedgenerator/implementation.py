import weakref


def cachedgenerator(func):
    def decorated(*args, **kwargs):
        generator = func(*args, **kwargs)
        return CachedGenerator(generator)

    return decorated


class CachedGenerator:
    so_far = weakref.WeakKeyDictionary()
    exhausted = weakref.WeakKeyDictionary()

    def __init__(self, generator):
        self.generator = generator
        self.so_far[self] = []
        self.exhausted[self] = False

    def __iter__(self):
        if self.exhausted[self]:
            yield from self.so_far[self]

        while True:
            try:
                next_item = next(self.generator)
                self.so_far[self].append(next_item)
                yield next_item

            except StopIteration:
                self.exhausted[self] = True
                break
