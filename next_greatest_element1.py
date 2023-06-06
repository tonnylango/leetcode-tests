def nge(array: list):
    stack = []
    result = []

    for value in array:
        while stack and stack[-1] < value:
            result.append((stack.pop(), value))
        stack.append(value)

    while stack:
        result.append((stack.pop(), -1))

    for value1, value2 in result:
        print(f"{value1} -> {value2}")
