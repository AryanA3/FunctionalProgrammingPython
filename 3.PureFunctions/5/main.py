def add_format(default_formats, new_format):
    default_formats = default_formats.copy()
    default_formats[new_format] = True
    return default_formats


def remove_format(default_formats, old_format):
    default_formats = default_formats.copy()
    default_formats[old_format] = False
    return default_formats