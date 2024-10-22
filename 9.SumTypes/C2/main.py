from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def check_if_line(edit, doc_len):
    if edit.get('line_number' , -1) != -1:
        if edit['line_number'] >= doc_len:
            raise Exception("Invalid line number") 

def check_if_start(edit, doc_len):
        if edit['start'] > doc_len:
            raise Exception("Invalid start index") 

def check_if_end(edit, doc_len):
        if edit['end'] > doc_len or edit['end'] < edit['start']:
            raise Exception("Invalid end index") 



def handle_edit(document, edit_type, edit):
    doc = document.split('\n')
    doc_len = len(doc)

    check_if_line(edit, doc_len)

    match edit_type:
        case EditType.NEWLINE:
            doc[edit['line_number']] = doc[edit['line_number']] + '\n'


        case EditType.SUBSTITUTE:
            line_len = len(doc[edit['line_number']])
            check_if_start(edit, line_len)
            check_if_end(edit, line_len)
            doc[edit['line_number']] = doc[edit['line_number']][:edit['start']] + edit['insert_text'] + doc[edit['line_number']][edit['end']:]
            

        case EditType.INSERT:
            line_len = len(doc[edit['line_number']])
            check_if_start(edit, line_len)
            doc[edit['line_number']] = doc[edit['line_number']][:edit['start']] + edit['insert_text'] + doc[edit['line_number']][edit['start']+ len(edit['insert_text']) : ]


        case EditType.DELETE:
            line_len = len(doc[edit['line_number']])
            check_if_start(edit, line_len)
            check_if_end(edit, line_len)
            doc[edit['line_number']] = doc[edit['line_number']][:edit['start']] + doc[edit['line_number']][edit['end'] : ]

        case _:
            raise Exception("Unknown edit type")

    return '\n'.join(doc)




# their code:

def handle_edit_sol(document, edit_type, edit):
    match edit_type:
        case EditType.SUBSTITUTE:
            return substitute(document, **edit)
        case EditType.INSERT:
            return insert(document, **edit)
        case EditType.DELETE:
            return delete(document, **edit)
        case EditType.NEWLINE:
            return newline(document, **edit)
        case _:
            raise Exception("Unknown edit type")


def newline(document, line_number):
    lines = document.split("\n")
    if len(lines) <= line_number:
        raise Exception("Invalid line number")
    line = lines[line_number]
    lines[line_number] = line + "\n"
    return "\n".join(lines)


def substitute(document, insert_text, line_number, start, end):
    lines = document.split("\n")
    if len(lines) <= line_number:
        raise Exception("Invalid line number")
    line = lines[line_number]
    if start > len(line):
        raise Exception("Invalid start index")
    if end > len(line) or end < start:
        raise Exception("Invalid end index")
    lines[line_number] = line[:start] + insert_text + line[end:]
    return "\n".join(lines)


def insert(document, insert_text, line_number, start):
    return substitute(document, insert_text, line_number, start, start)


def delete(document, line_number, start, end):
    return substitute(document, "", line_number, start, end)