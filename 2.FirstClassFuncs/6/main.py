def remove_invalid_lines(document):
    return '\n'.join(filter(lambda x: '-' not in x , document.split('\n')))