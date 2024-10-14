def sum_nested_list(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):
           total += sum_nested_list(i)
        else:
            total += i
    return total