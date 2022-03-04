class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        #print(l1.next.val, l2.next.val)
        carry = 0
        outlist = None
        cur3 = outlist
        while((l1 != None) and (l2 != None)):
            sum = l1.val + l2.val + carry
            #print("Sum = ",sum)
            carry = sum // 10
            sum = sum % 10
            insert_node = ListNode(sum)
            #print("Insert Node = ",insert_node.val)
            if(outlist == None):
                outlist = insert_node
                cur3 = outlist
            else:
                cur3.next = insert_node
                cur3 = cur3.next
            l1 = l1.next
            l2 = l2.next

        if(l1 == None):
            present = l2
        elif(l2 == None):
            present = l1
        while(present != None):
            sum = present.val + carry
            carry = sum // 10
            sum = sum % 10
            insert_node = ListNode(sum)
            cur3.next = insert_node
            cur3 = cur3.next
            present = present.next
        
        if(carry > 0):
            insert_node = ListNode(carry)
            cur3.next = insert_node
            
        return outlist

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n1.next.next.next = ListNode(4)

n2 = ListNode(5)
n2.next = ListNode(6)
n2.next.next = ListNode(7)
#n2.next.next.next = ListNode(9)

ob = Solution()

n3 = ob.addTwoNumbers(n1,n2)

print(n3.val, n3.next.val, n3.next.next.val, n3.next.next.next.val)
print()
print(n1.val, n1.next)       
            

