# Only Positive Numbers (E)
# Define a function that takes as parameter list of numbers and returns the list 
# containing only the numbers that are greater than 0. For example, I called your 
# function with foo([-5, 3, -1, 101]) it should return [3, 101].

def only_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

# Example usage:
result = only_positive_numbers([-5, 3, -1, 101])
print(result)  # Output: [3, 101]
