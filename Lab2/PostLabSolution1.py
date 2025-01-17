# Calculate the mean of a List
def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Calculate the median of a List
def median(numbers):
    if not numbers:
        raise ValueError("The list is empty. Cannot compute the median.")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:  
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:  
        return sorted_numbers[mid]

# Calculate the mode of a List
def mode(numbers):
    if not numbers:
        raise ValueError("The list is empty. Cannot compute the mode.")
    
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_freq = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_freq]

    return min(modes)  

if __name__ == "__main__":
    test_data = [4, 1, 2, 2, 3, 5, 4]

    # Calculate and print the mean
    mean_result = calculate_mean(test_data)
    print(f"Mean: {mean_result}")

    # Calculate and print the median
    median_result = median(test_data)
    print(f"Median: {median_result}")

    # Calculate and print the mode
    mode_result = mode(test_data)
    print(f"Mode: {mode_result}")
