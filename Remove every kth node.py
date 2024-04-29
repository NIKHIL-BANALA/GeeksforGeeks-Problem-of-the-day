class Solution:
    def deleteK(self, head, k):
        #code here  
        if k == 1:
            return
        node = head
        count = 1
        while node and node.next:
            if count == k-1:
                count = 1
                node.next = node.next.next
            else:
                count+=1
            node = node.next
        return head