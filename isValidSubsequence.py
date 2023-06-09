def check(array, sequence):
    try:
        position = 0
        for i in range(0, len(sequence)):
            print(f"sequence[{i}]:", sequence[i], " position:", position)
            
            position += array[position:].index(sequence[i])
            print(f"position of sequnce[{i}] in array {position}")
            position += 1
        return True
    except Exception:
        return False

def check2(array, sequence):
    # Loop through the array in reverse order
    for i in range(len(array) - 1, -1, -1):
        if len(sequence) == 0:
            break  # Stop the loop if the sequence is empty
        if array[i] == sequence[-1]:  # Check if current element matches the last element in the sequence
            sequence.pop()  # Remove the last element from the sequence

    return return not sequence
 # Return True if the sequence is empty, otherwise False


if __name__ == "__main__":
    array = [1,1,1,6]
    sequence = [1,1,1,1]

    print(check2(array, sequence))
