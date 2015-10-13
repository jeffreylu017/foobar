def foo(a, b):
    return a + b

def filter(pred, iterable):
    for el in iterable:
        if pred(el):
            yield el

def badfilter(pred, iterable):
    for el in iterable:
        yield el

