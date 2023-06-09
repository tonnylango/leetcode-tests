def method(array, target):
    print("array ", array, " target ", target)
    if target in array:
        return [[target]]  # Return target as a list
    array = [element for element in array if element < target]  # Remove large elements from array
    if not array or sum(array) < target:
        return [[]]  # Return an empty list if array is empty or sum of elements is less than target
    if sum(array) == target:
        return [array]

    answers = set()  # Initialize list answers

    for number in array:
        remaining_array = array.copy()
        remaining_array.remove(number)
        returned_answers = method(remaining_array, target - number)
        for returned_answer in returned_answers:
            returned_answer.append(number)
            if sum(returned_answer) == target:
                answers.add(tuple(returned_answer)) #convert the list to a tuple to make it hashable and then add it to answers

    answers = [list(sublist) for sublist in answers]
    return answers

import sys

if __name__ == "__main__":
    #Extract array and target from command-line arguments
    arguments = sys.argv[1:]
    array = [int(arg) for arg in arguments[:-1]]
    target = int(arguments[-1]) 

    result = method(array, target)
    print(result)                               
        
