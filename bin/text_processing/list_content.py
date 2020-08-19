from datetime import date, timedelta

def format_date(date):
    return date.strftime('%d/%m/%Y')

def insert_dates(df):
    today = date.today()
    friday = today + timedelta((4 - today.weekday()) % 7)

    df.at[0, 4] = 'Conversiedatum'
    df.at[0, 5] = format_date(today)

    df.at[1, 4] = 'Aanstaande vrijdag'
    df.at[1, 5] = format_date(friday)

    return df
