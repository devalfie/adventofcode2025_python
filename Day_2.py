def is_invalid_part1(num_str):
    """
    Part 1: ID is invalid if it's made of a sequence repeated exactly twice.
    E.g., 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
    """
    n = len(num_str)
    # The sequence length must be half the total length
    if n % 2 != 0:
        return False
    
    half = n // 2
    first_half = num_str[:half]
    second_half = num_str[half:]
    
    return first_half == second_half


def is_invalid_part2(num_str):
    """
    Part 2: ID is invalid if it's made of a sequence repeated at least twice.
    E.g., 12341234 (1234 twice), 123123123 (123 three times), 1212121212 (12 five times)
    """
    n = len(num_str)
    
    # Try all possible sequence lengths from 1 to n//2
    for seq_len in range(1, n // 2 + 1):
        if n % seq_len == 0:
            # Check if the number is made of this sequence repeated
            sequence = num_str[:seq_len]
            repetitions = n // seq_len
            
            if repetitions >= 2 and sequence * repetitions == num_str:
                return True
    
    return False


def solve_part1(ranges):
    """Find all invalid IDs in the ranges (Part 1 rules)"""
    total = 0
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_part1(str(num)):
                total += num
    
    return total


def solve_part2(ranges):
    """Find all invalid IDs in the ranges (Part 2 rules)"""
    total = 0
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_part2(str(num)):
                total += num
    
    return total


# Read input
with open('../day2.txt', 'r') as f:
    line = f.read().strip()

# Parse ranges
ranges = []
for range_str in line.split(','):
    start, end = map(int, range_str.split('-'))
    ranges.append((start, end))

# Solve both parts
part1_answer = solve_part1(ranges)
part2_answer = solve_part2(ranges)

print(f"Part 1: {part1_answer}")
print(f"Part 2: {part2_answer}")
