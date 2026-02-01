# Only Numbers (E)
# Define a function that takes as a parameter a list that contains both integers and 
# strings and returns the list containing only the integers. For example, if I called 
# your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].

def only_numbers(parameters):
    return [parameter for parameter in parameters if type(parameter) == int]

# Example usage:
result = only_numbers([99, 'no data', 95, 94, 'no data'])
print(result)  # Output: [99, 95, 94]
