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

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        results = []
        p1, p2 = l1, l2
        carry = 0

        while p1 and p2:
            r = p1.val + p2.val + carry
            carry = r // 10
            results.append(r % 10)
            p1, p2 = p1.next, p2.next

        longer_node = p1 or p2

        while longer_node:
            r = longer_node.val + carry
            carry = r // 10
            results.append(r % 10)
            longer_node = longer_node.next

        if carry:
            results.append(carry)

        result_node = ListNode(results[0])
        p = result_node
        for value in results[1:]:
            p.next = ListNode(value)
            p = p.next

        return result_node

#solution 2
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        results = ListNode(0)
        pointer = results
        carry = 0

        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            pointer.next = ListNode(sum % 10)
            pointer = pointer.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None

        return results.next
