

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Rotate:
    def rotate_right(self,head,k):
        n = 0 # find length ,k is no times last moved to front
        temp = head # start point
        while(temp): # untill head is not none
            temp = temp.next
            n += 1

        k = k%n
        for i in range(k):
            prev = None
            curr = head
            while(curr.next != None): # travers1 2 3 4 5 6 none
                prev = curr #  make prev 5
                curr = curr.next #  make curr as 6 and move to next

            prev.next = None # break the link
            curr.next = head # link the last node 6 to head
            head = curr # 6

        return head





