class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = ListNode(val=None)
        tail = list3

        while list1 is not None:
            tail.next = ListNode(list1.val)
            tail = tail.next
            list1 = list1.next

        while list2 is not None:
            tail.next = ListNode(list2.val)
            tail = tail.next
            list2 = list2.next

        if not list3 or not list3.next:
            return list3.next
    
        swapped = True

        while swapped:
            swapped = False
            current = list3

            while current and current.next:
                if current.val > current.next.val:
                    current.val, current.next.val = current.next.val, current.val
                    swapped = True
                current = current.next

        return list3.next
        