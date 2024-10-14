from functools import reduce


def paginator(page_length):
    def paginate(document):
        words = document.split()

        def add_word_to_pages(pages, word):
            if pages == None or pages == []:
                return [word]

            if (len(pages[-1]) + len(word) + 1 ) > page_length:
                pages.append(word)
            else:
                pages[-1] += ' ' + word
                
            return pages

        return reduce(add_word_to_pages, words, [])

    return paginate