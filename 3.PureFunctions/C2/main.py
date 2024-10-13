from datetime import date

def sort_dates(dates):
    return list(map(convert_date_to_str , sorted(map(convert_str_to_date, dates))))

def convert_str_to_date(d):
    return date(int(d[6:]),int(d[0:2]),int(d[3:5]))

def convert_date_to_str(d):
    return d.strftime('%m-%d-%Y')



# Proivided:

# def sort_dates(dates):
#     return sorted(dates, key=format_date)


# def format_date(date):
#     month, day, year = date.split("-")
#     return year + month + day