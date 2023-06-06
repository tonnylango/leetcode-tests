def method(array, target):
    print("array ", array, " target ", target)
    if target in array:
        return [[target]]  # Return target as a list
    array = [element for element in array if element < target]  # Remove large elements from array
    if not array or sum(array) < target:
        return [[]]  # Return an empty list if array is empty or sum of elements is less than target
    if sum(array) == target:
        return [array]

    answers = []  # Initialize list answers

    for number in array:
        remaining_array = array.copy()
        remaining_array.remove(number)
        returned_answers = method(remaining_array, target - number)
        print("returned_answers", returned_answers, "for array ", array, " target ", target)
        for returned_answer in returned_answers:
            print("returned_answer ", returned_answer, type(returned_answer))
            returned_answer.append(number)
            if sum(returned_answer) == target:
                answers.append(returned_answer)
    
    return answers

import sys

if __name__ == "__main__":
    #Extract array and target from command-line arguments
    arguments = sys.argv[1:]
    array = [int(arg) for arg in arguments[:-1]]
    target = int(arguments[-1]) 

    result = method(array, target)
    print(result)                               
        
