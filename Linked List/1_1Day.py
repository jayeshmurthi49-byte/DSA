# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


def reverselist(head):
    prev = None
    curr = head


    while curr:
        next = curr.next 
        curr.next = prev
        prev = curr
        curr = next

    return prev