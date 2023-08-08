def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

number = int(input("Enter a number: "))
fibonacci_sequence = generate_fibonacci_sequence(number)
print(fibonacci_sequence)