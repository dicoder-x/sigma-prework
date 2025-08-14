import datetime


def years(date_string):
    '''
    First attempt (simple answer):
    Using a string of format YYYY-MM-DD return difference in years (from today),
    doesn't consider if Birthday hasn't passed yet
    Returns difference in years between today and input
    '''
    try:
        date_list = date_string.split('-')
        return (datetime.date.today() - datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))).days // 365
    except (TypeError, ValueError):
        print("Invalid date format.")


def difference(date_string):
    '''
    Second attempt (advanced):
    Enables the most commonly used formats to be taken as argument, checks if Birthday has passed.
    If both day & month <= 12: Day Month Year order is assumed e.g. (06 05 2001) is 6th May 2001, 
    use name of month to resolve (June 05 2001).
    Returns difference between today and input date in years
    '''
    formats = [
        "%Y-%m-%d",            # 2025-08-14
        "%d-%m-%Y",            # 14-08-2025
        "%m-%d-%Y",            # 08-14-2025
        "%d/%m/%Y",            # 14/08/2025
        "%m/%d/%Y",            # 08/14/2025
        "%d %m %Y",            # 14 08 2025
        "%m %d %Y",            # 08 14 2025
        "%Y %m %d",            # 2025 08 14
        "%Y/%m/%d",            # 2025/08/14
        "%Y.%m.%d",            # 2025.08.14
        "%d.%m.%Y",            # 14.08.2025
        "%d %b %Y",            # 14 Aug 2025
        "%d %B %Y",            # 14 August 2025
        "%b %d %Y",            # Aug 14 2025
        "%B %d %Y",            # August 14 2025
        "%B %d, %Y",           # August 14, 2025
        "%b %d, %Y",           # Aug 14, 2025
        "%Y%m%d",              # 20250814
        "%d%m%Y",              # 14082025
        "%m%d%Y",]              # 08142025

    date_input = None
    for format in formats:  # Loop through formats, break loop once valid format found
        try:
            date_input = datetime.datetime.strptime(date_string, format).date()
            break
        except (ValueError):
            continue

    if date_input == None:
        print("Invalid date format.")
    elif (datetime.date.today().month, datetime.date.today().day) < (date_input.month, date_input.day):
        # If Birthday hasn't passed yet, subtract 1 from difference
        return ((datetime.date.today() - date_input).days // 365) - 1
    else:
        return (datetime.date.today() - date_input).days // 365


output = difference(input("Enter your Birthday (DD MM YYYY): "))
print(output)
