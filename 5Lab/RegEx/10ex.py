def camel_to_snake(camel_case):
    snake_case = ''
    for i in range(len(camel_case)):
        if camel_case[i].isupper() and i > 0:
            snake_case += '_'
        snake_case += camel_case[i].lower()
    return snake_case

camel_case = 'ConvertGivenCamelCaseStringToSnakeCase'
snake_case = camel_to_snake(camel_case)

print(snake_case)