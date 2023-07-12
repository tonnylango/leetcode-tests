import re


def camel_to_snake_case(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

def camel_to_snake_case(string):
    ls = list(string)
    ls[0] = ls[0] if ls[0].islower() else ls[0].lower()
    convert_to_lower = lambda x: "_" + x.lower() if x.isalpha() and not x.islower() else x

    rs = "".join(list(map(convert_to_lower, ls)))
    
    return rs
    

# Define test cases
test_cases = [
    (['camelCaseString', 'anotherExample', 'helloWorld'], ['camel_case_string', 'another_example', 'hello_world']),
    (['SingleWord', 'example', 'TEST'], ['single_word', 'example', 'test']),
    (['HTMLParser', 'APIRequest', 'HTTPResponse'], ['html_parser', 'api_request', 'http_response']),
    (['example123', 'camel123Case', 'myValue1'], ['example123', 'camel123_case', 'my_value1']),
    ([], []),
    (['MixedCaseString', 'notcamelcase', 'Another_Case'], ['mixed_case_string', 'notcamelcase', 'another_case'])
]

# Run the test cases
for i, (input_list, expected_output) in enumerate(test_cases, 1):
    for input_str, expected_str in zip(input_list, expected_output):
        actual_str = camel_to_snake_case(input_str)
        if actual_str != expected_str:
            print(f"{i} {input_str} failed. Expected: {expected_str}, but got: {actual_str}")
        else:
            print(f"{i} {input_str} passed. Got {expected_str}")