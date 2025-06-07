def calculate_even_numbers():
    even_numbers = [num for num in range(1, 1001) if num % 2 == 0]
    sum_of_evens = sum(even_numbers)
    average_of_evens = sum_of_evens / len(even_numbers)
    square_of_sum = sum_of_evens ** 2

    return average_of_evens, square_of_sum

# Calculate and print the results
average, square_of_sum = calculate_even_numbers()
print(f"Average of even numbers between 1 and 1000: {average}")
print(f"Square of the sum of even numbers between 1 and 1000: {square_of_sum}")