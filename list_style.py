def color_rows(series):
    return [
        'background-color: #D3D3D3'
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

def resize_columns(series):
    return ['width: 500px' for value in series]