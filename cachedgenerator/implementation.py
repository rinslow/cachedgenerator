import inspect


def cachedgenerator(func):
    def meow(*args, **kwargs):
        generator = func(*args, **kwargs)
        return CachedGenerator(generator)
    return meow


class CachedGenerator:
    def __init__(self, generator):
        self.generator = generator
        self.so_far = []
        self.exhausted = False

    def __iter__(self):
        if self.exhausted:
            for item in self.so_far:
                yield item

        else:
            try:
                next_item = next(self.generator)
                self.so_far.append(next_item)
                yield next_item

            except StopIteration:
                self.exhausted = True
                for item in self:
                    yield item
