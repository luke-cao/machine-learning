NOT_VALID = ['不合法！']


def get_contents(expression):
    if expression.count('(') != expression.count(')'):
        return NOT_VALID
    ret = []
    stack = []
    for idx, item in enumerate(expression):
        if item == '(':
            stack.append((idx, item))
        elif item == ')':
            # compare to last item
            # if no last item, means that no opening parenthesis but have closing parenthesis
            try:
                last_item = stack.pop()
            except IndexError as e:
                return NOT_VALID
            # if last item is present, then remove it and append content to list ret
            ret.append(expression[last_item[0]: idx + 1])
    return ret


def main():
    while True:
        expression = input()
        if expression == 'stop':
            break
        contents = get_contents(expression)
        print(*contents, sep='\n')


if __name__ == '__main__':
    main()