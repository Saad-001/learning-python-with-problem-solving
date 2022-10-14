# linked list implementation using python
# https://ideone.com/DqhhHW

class Node :
    def __init__(self, val) :
        self.value = val
        self.next = None

class Linked_list :

    def __init__(self) :
         self.head = None

    def insert_at_pos(self, pos, val) :
        newNode = Node(val)
        if pos == 0 :
            newNode.next = self.head
            self.head = newNode
        else :
            tmp = self.head
            for i in range(pos - 1) :
                tmp = tmp.next
                if tmp == None :
                    print("cannot insert node")
                    return

            newNode.next = tmp.next
            tmp.next = newNode

    def insert_at_tail(self, val) :
        newNode = Node(val)
        if self.head == None :
            self.head = newNode
        else : 
            tmp = self.head
            while tmp.next != None :
                tmp = tmp.next

            tmp.next = newNode

    def delete_at_pos(self, pos) :
        if pos == 0 :
            delNode = self.head
            self.head = self.head.next
            del delNode
        else :
            tmp = self.head
            for i in range(pos - 1) :
                tmp = tmp.next
            if tmp == None :
                print("out of bound")
                return
            delNode = tmp.next
            if tmp.next == None :
                print("out of bound")
                return
            else :
                tmp.next = tmp.next.next
                del delNode

    def reverse(self) :
        if self.head.next == None :
            return self.head
        save = self.head    
        self.head = self.head.next
        newHead = self.reverse()
        save.next.next = save
        save.next = None
        return newHead

    def print_list(self) :
        tmp = self.head
        while tmp != None :
            print(tmp.value)
            tmp = tmp.next

def main () :
    lst = Linked_list()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(30)
    lst.insert_at_pos(2, 40)
    lst.delete_at_pos(2)
    lst.head = lst.reverse()
    lst.print_list()


main()
 