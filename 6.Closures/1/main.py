def word_count_aggregator():
    count = 0
    def count_word(doc):
        nonlocal count
        for line in doc.split('\n'):
            count += len(line.split(' ')[0:])
        return count
    return count_word