# Zeros Instead (E)
# Define a function that takes as parameter a list that contains both numbers and 
# strings and returns the same list but with zeros instead of strings. For example, 
# I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 0, 95, 94, 0].

def zeros_instead(parameters):
    return [parameter if type(parameter) == int else 0 for parameter in parameters]

# Example usage:
result = zeros_instead([99, 'no data', 95, 94, 'no data'])
print(result)  # Output: [99, 0, 95, 94, 0]
