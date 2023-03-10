from functools import reduce
def multiply_list_numbers(numbers):
    product = reduce((lambda x, y: x * y), numbers)
    return product
numbers = [2, 4, 6, 8, 10]
result = multiply_list_numbers(numbers)
print(result)