class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        n1 = ""
        while num1:
            n1+=str(num1.data)
            num1 = num1.next
        n2 = ""
        while num2:
            n2+=str(num2.data)
            num2 = num2.next
        n1,n2 = int(n1), int(n2)
        ans = str(n1+n2)
        num1 = Node(int(ans[0]))
        node = num1
        for i in range(1,len(ans)):
            temp = Node(int(ans[i]))
            node.next = temp
            node = temp
        return num1