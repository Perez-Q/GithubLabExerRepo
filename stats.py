# Calculate the mean of a List
def mean(numbers):
    if not numbers:
        raise ValueError("The list is empty. Cannot compute the mean.")
    return sum(numbers) / len(numbers)

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

# Example usage:
if __name__ == "__main__":
    data = [4, 1, 2, 2, 3, 5, 4]
    print("Mean:", mean(data))  # Output: Mean
    print("Median:", median(data))  # Output: Median
    print("Mode:", mode(data))  # Output: Mode
