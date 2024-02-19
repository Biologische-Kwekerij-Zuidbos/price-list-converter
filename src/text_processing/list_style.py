def style_dataframe(df):
    return df.style \
        .apply(color_rows, axis=0)

def color_rows(series):
    return [
        'background-color: #e6e6e6'
        if index % 2 == 0 and index > 5 else ''
        for index, _ in enumerate(series)
    ]