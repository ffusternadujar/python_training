def convert_and_sum_up(parameters):
    return sum([float(parameter)if type(parameter) == str else 0 for parameter in parameters])

# Example usage:
result = convert_and_sum_up([10, '20.5', 5.5, '30'])
print(result)  # Output: 50.5

def process_strings(*args):
    list = [string.upper() for string in args]
    list.sort()
    return list.sort()

# Example usage:
result = process_strings('apple', 'banana', 'cherry')
print(result)  # Output: ['APPLE', 'BANANA', 'CHERRY']
