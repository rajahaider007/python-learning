# # fuction in python
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b
# def calculator(a, b, operation):
#     if operation == "add":
#         return add(a, b)
#     elif operation == "subtract":
#         return subtract(a, b)
#     elif operation == "multiply":
#         return multiply(a, b)
#     elif operation == "divide":
#         return divide(a, b)
#     else:
#         return "Invalid operation"
# # Example usage
# a = 10
# b = 5
# operation = "add"
# result = calculator(a, b, operation)
# print(f"The result of {operation}ing {a} and {b} is: {result}")
# # Example usage
# a = 10
# b = 5
# operation = "subtract"
# result = calculator(a, b, operation)
# print(f"The result of {operation}ing {a} and {b} is: {result}")
# # Example usage
# a = 10
# b = 5
# operation = "multiply"
# result = calculator(a, b, operation)
# print(f"The result of {operation}ing {a} and {b} is: {result}")
# # Example usage
# a = 10
# b = 5
# operation = "divide"
# result = calculator(a, b, operation)
# print(f"The result of {operation}ing {a} and {b} is: {result}")

#recursion in python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Example usage
n = 5
result = factorial(n)
print(f"The factorial of {n} is: {result}")