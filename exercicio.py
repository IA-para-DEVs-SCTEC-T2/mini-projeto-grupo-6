def has_duplicate(lst):
    seen = set()
    return any(x in seen or seen.add(x) for x in lst)