def foo(a, b):
    return a + b

def filter(pred, iterable):
    for el in iterable:
        if pred(el):
            yield el

def badfilter(pred, iterable):
    for el in iterable:
        if pred(el):
            yield el

class Baz(object):
    def untested(self):
        1/0

    def donottest(self):
        assert False

    def tested(self, alfalfa):
        while alfalfa > 0:
            alfalfa -= 1
        return 1

