import functools


def join(doc_so_far, sentence):
    return f"{doc_so_far}. {sentence}"


def join_first_sentences(sentences, n):
    if n == 0:
        return ""

    reduced = functools.reduce(join, sentences[:n])
    return reduced + '.'