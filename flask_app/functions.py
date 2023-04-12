from datetime import datetime


def date_to_str(date_float):
    date_dt = datetime.fromordinal(int(date_float))
    date_str=date_dt.strftime('%Y-%m-%d')
    return date_str


def date_to_float(date_str):
    date_dt = datetime.strptime(date_str,'%Y-%m-%d')
    date_float = datetime.toordinal(date_dt)
    return date_float