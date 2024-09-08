# print("Big O notation is the way to measure how software program's running time or space requirements grow as the input size grows. We can't measure this using absolute terms such as time in seconds because different computers have different hardware hence we need a mathematical way to measure time complexity of a program and Big O is that mathematical way. The basic idea is to come up with mathematical function for a running time and consider only fastest growing term and discard other terms as well as constants. Big O is used to measure space complexity as well, You will know how to find the time and space complexity of algorithms.")

# time = a*n + b
# time = a*n
# time = O(n)

def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers


numbers = [2,5,8,9, 10,11,12,13,14,15]
print(get_squared_numbers(numbers))

# time = O(n^2)