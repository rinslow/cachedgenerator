def cachedgenerator(func):
    def decorated(*args, **kwargs):
        generator = func(*args, **kwargs)
        return CachedGenerator(generator)

    return decorated


class CachedGenerator:
    def __init__(self, generator):
        self.generator = generator
        self.so_far = []
        self.exhausted = False

    def __iter__(self):
        if self.exhausted:
            yield from self.so_far

        while True:
            try:
                next_item = next(self.generator)
                self.so_far.append(next_item)
                yield next_item

            except StopIteration:
                self.exhausted = True
                break
