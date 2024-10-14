def find_longest_word(document, longest_word=""):
    if document == '':
        return longest_word
    
    splitted = document.split(' ')
    return find_longest_word(' '.join(splitted[1:]), longest_word if len(splitted[0]) <= len(longest_word) else splitted[0])
