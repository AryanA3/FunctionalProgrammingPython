def deduplicate_lists(lst1:list, lst2:list, reverse=False):
    return sorted(set(lst1 + lst2), reverse=reverse)