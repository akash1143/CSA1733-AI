import itertools

def solve_cryptarithm(sum1, sum2, total):
    # Extract unique characters
    unique_chars = set(sum1 + sum2 + total)
    
    # Check for impossible conditions
    if len(unique_chars) > 10:
        return "Too many different letters. No solution possible."

    # Try all permutations of digits assigned to letters
    for perm in itertools.permutations('0123456789', len(unique_chars)):
        # Map letters to digits
        char_to_digit = dict(zip(unique_chars, perm))
        
        # Convert words to numbers based on the current mapping
        num1 = int(''.join(char_to_digit[c] for c in sum1))
        num2 = int(''.join(char_to_digit[c] for c in sum2))
        num_total = int(''.join(char_to_digit[c] for c in total))

        # Check if the current mapping solves the equation
        if num1 + num2 == num_total:
            # Ensure no leading zero issue
            if (char_to_digit[sum1[0]] != '0' and 
                char_to_digit[sum2[0]] != '0' and 
                char_to_digit[total[0]] != '0'):
                return char_to_digit

    return "No solution found."

# Accept user input for the problem
sum1 = input("Enter the first summand (word): ")
sum2 = input("Enter the second summand (word): ")
total = input("Enter the sum total (word): ")

solution = solve_cryptarithm(sum1, sum2, total)

if isinstance(solution, dict):
    print("Solution found:")
    print(', '.join(f'{k} = {v}' for k, v in solution.items()))
else:
    print(solution)
