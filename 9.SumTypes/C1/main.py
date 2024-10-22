from enum import Enum
from functools import reduce


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            return ("Pending..." , list(map(lambda x: list(map(lambda y: str(y) , x)) , data)))

        case CSVExportStatus.PROCESSING:
            return ("Processing..." , reduce(lambda acc, next: acc + ','.join(next) + '\n', data, "")[:-1])

        case CSVExportStatus.SUCCESS:
            return ("Success!" , data)

        case CSVExportStatus.FAILURE:
            pen = list(map(lambda x: map(lambda y: str(y) , x) , data))
            pros = reduce(lambda acc, next: acc + ','.join(next) + '\n', pen, "")[:-1]
            return ("Unknown error, retrying..." , pros)

        case _:
            raise Exception("Unknown export status")
        

#THEIR CODE:


def get_csv_status_solution(status, data):
    match status:
        case CSVExportStatus.PENDING:
            return prepare(data)
        case CSVExportStatus.PROCESSING:
            return process(data)
        case CSVExportStatus.SUCCESS:
            return handle_success(data)
        case CSVExportStatus.FAILURE:
            return handle_failure(data)

def prepare(data):
    processed_data = list(map(lambda lst: list(map(lambda s: str(s), lst)), data))
    return "Pending...", processed_data


def process(prepared_data):
    processed_data = "\n".join(map(lambda lst: ",".join(lst), prepared_data))
    return "Processing...", processed_data


def handle_success(processed_data):
    return "Success!", processed_data


def handle_failure(data):
    _, processed_data = process(prepare(data)[1])
    return "Unknown error, retrying...", processed_data
