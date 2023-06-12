def check(array, sequence):
    try:
        position = 0
        for i in range(0, len(sequence)):
            print(f"sequence[{i}]:", sequence[i], " position:", position)
            
            #position += array[position:].index(sequence[i])
            position += array.index(sequence[i], position)
            position += 1 #so as to start searching array from the next element after the current
        return True
    except Exception:
        return False

#this mutates the sequence array, which may result in unexpected behavior, ensure array is copied.
def check2(array, sequence):
    # Loop through the array in reverse order
    for i in range(len(array) - 1, -1, -1):
        if len(sequence) == 0:
            break  # Stop the loop if the sequence is empty
        if array[i] == sequence[-1]:  # Check if current element matches the last element in the sequence
            sequence.pop()  # Remove the last element from the sequence

    # Return True if the sequence is empty, otherwise False
    return not sequence
 


if __name__ == "__main__":
    array = [1,1,1,6]
    sequence = [1,1,1,1]

    print(check(array, sequence))
