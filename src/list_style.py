def style_dataframe(df):
    return df.style \
        .apply(color_rows, axis=0) \
        .apply(color_head, axis=0) \
        .apply(color_head_text, axis=0)

def color_rows(series):
    return [
        'background-color: #e6e6e6'
        if index % 2 == 0 and index > 5 else ''
        for index, _ in enumerate(series)
    ]

def color_head(series):
    return [
        'background-color: grey'
        if index == 5 else ''
        for index, _ in enumerate(series)
    ]

def color_head_text(series):
    return [
        'color: white'
        if index == 5 else ''
        for index, _ in enumerate(series)
    ]