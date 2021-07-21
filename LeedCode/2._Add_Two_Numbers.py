# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        returnNode1 = l1
        returnNode2 = l2
        preValue = 0
        ck = True

        while l1 is not None or l2 is not None:
            l1Value = 0
            l2Value = 0

            if l1 is not None:
                l1Value = l1.val
            if l2 is not None:
                l2Value = l2.val

            updateValue = (l1Value + l2Value + preValue)
            preValue = updateValue // 10
            updateValue %= 10

            if l1 is not None:
                l1.val = updateValue
                l1 = l1.next
                ck = True
            if l2 is not None:
                l2.val = updateValue
                l2 = l2.next
                ck = False

        if ck:
            returnNode = returnNode1
        else:
            returnNode = returnNode2
        returnNodeHead = returnNode
        while returnNode.next:
            returnNode = returnNode.next

        while preValue > 0:
            returnNode.next = ListNode(preValue % 10)
            if preValue < 10:
                break
            preValue //= 10

        return returnNodeHead