def file_type_getter(file_extension_tuples):
    extentions = {}
    for i in file_extension_tuples:
        for j in i[1]:
            extentions[j] = i[0]

    return lambda x: extentions.get(x, "Unknown")