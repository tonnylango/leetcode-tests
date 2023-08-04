def add(p1, p2):
    result = []
    carry = 0
    
    p1.extend([0] * (len(p2) - len(p1))) if len(p1) < len(p2) else p2.extend([0] * (len(p1) - len(p2)))

    for v1, v2 in zip(p1, p2):
        r = v1 + v2 + carry
        carry = r // 10
        result.append(r % 10)
        
    if carry:
        result.append(carry)
        
    return result
    
print(add([9,9,9,9,9,9,9], [9,9,9,9]))
print(add([0], [0]))
print(add([2, 4, 3], [5, 6, 4]))  # Should print [7, 0, 8]
print(add([9, 9, 9], [1]))       # Should print [0, 0, 0, 1]
print(add([1, 2, 3], [4, 5, 6])) # Should print [5, 7, 9]