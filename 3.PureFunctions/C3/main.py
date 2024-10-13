def index_keywords(document, index):
    index = index.copy()
    if document in index:
        return index[document], index
    found_keywords = find_keywords(document)
    index[document] = found_keywords
    return found_keywords, index


def find_keywords(document):
    keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
    ]
    return list(filter(lambda keyword: keyword in document, keywords))
   