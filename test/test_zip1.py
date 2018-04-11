def zip1(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

def hello():
    print('hello')
    print('hello')

hello()


a = zip1('ABCD', 'xy')
print(a)
print('a')