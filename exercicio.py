def has_duplicate(lst):
    return len(array) != len(set(array))

def has_duplicate_refactor(lst):
    seen = set()
    return any(x in seen or seen.add(x) for x in lst)