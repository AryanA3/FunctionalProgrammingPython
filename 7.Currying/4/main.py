import functools


def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_lenght(doc):
            splited = doc.split('\n')
            i = 0
            for j in splited:
                if sequence in j:
                    i += 1
            return i            
        return with_lenght
    return with_char