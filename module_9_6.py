def all_variants(text):
    from itertools import pairwise
    for i in text:
        yield i
    fgh = pairwise(text)
    for q in fgh:
        q = ''.join(list(q))
        yield q
    print(text)


a = all_variants("abc")
for g in a:
    print(g)
