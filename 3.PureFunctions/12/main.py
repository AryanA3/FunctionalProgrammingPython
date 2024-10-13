def word_count_memo(document, memos):
    if memos.get(document, -1) != -1:
        return memos[document], memos
    memos = memos.copy()
    wc = word_count(document)
    memos[document] = wc
    return wc, memos


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count