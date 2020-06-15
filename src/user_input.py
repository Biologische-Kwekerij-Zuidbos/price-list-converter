def ask(question):
    answer = input(
        question + ' (y/n) '
    ).lower()

    return len(answer) > 0 and answer[0] == 'y'