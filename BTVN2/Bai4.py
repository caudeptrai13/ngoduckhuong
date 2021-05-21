class Node:
    def __init__(self,num : int = 0, next = None):
        self.value = num
        self.next = next
    def __str__(self):
        p = self
        string = ""
        string += str(p.value)
        while(p.next != None):
            p = p.next
            string = string + " --> " + str(p.value)
        return string
    @staticmethod
    def takeFromList(array : list):
        p = Node(array[0])
        start = p
        for i in array[1:]:
            p.next = Node(i)
            p = p.next
        return start
    def getMiddle(self):
        slow = self
        fast = self
        while(fast != None and slow != None):
            fast = fast.next
            if (fast == None):
                break
            else:
                fast = fast.next
            slow = slow.next
        return slow.value
    def move(self,num : int):
        start = self
        k = 1
        p = start
        while(k < num):
            p = p.next
            k += 1
        new = p.next
        p.next = None
        p = new
        while(p.next != None):
            p = p.next
        p.next = start
        return new

print(Node.takeFromList([1,2,3,4,5,6,7,8]).move(4))
print(Node.takeFromList([1,2,3,4]).getMiddle())