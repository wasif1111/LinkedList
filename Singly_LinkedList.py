import os

try:
    from prettytable import PrettyTable
except:
    print("[ + ] Package/prettytable is not available.")
    print("Downloading pkg/prettytable")
    os.system("python -m pip install prettytable")
    from prettytable import PrettyTable  

class Node:
    """
        NODE
        Node is data Class for LinkedList Class.
        
        Attributes:
        data      This attribute can hold any type of the Data for a Node.
        next      This attribute holds the Reference of Next Node.
                  Default Value for __next attribute is {None}.
        Methods:
        Class contains only [CONSTRUCTURE] method for constructing the a node Attributes.
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    """
        LINKED LIST
        Class to perform various Operations
        
        Attributes:
        head            This Attribute holds the start Reference [Address] of LinkedList
        tail            This Attribute holds the end Reference [Address] of LinkedList
        length          This Attirbute holds the Lenght of the LinkedList

        Methods:
        1)  Append      : Append an Element in last of the Linked List
        2)  Prepend     : Append an Element in start of the Linked List
        3)  Insert      : Add an Element in the Linked List on given Index
        4)  Pop         : Remove the last Element from the Linked List
        5)  PopFirst    : Remove the first Element from the Linked List
        6)  Remove      : Remove the Element asked from given Index
        7)  getNode     : Return the Value of given Index
        8)  setNode     : Update the Value of a Node in given Index
        9)  PrintLL     : Display all members of Linked List
        10) Reverse     : Reverse the Linked List
        11) FC Algo     : Floyed Cycle Finding Algorithm [Detects if there is any loop Occurs in LL or not]
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        
        newNode = Node(data=data)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        print("[ + ] Node Added with Value :: ", data)
            
    def pop(self):
        
        if self.length == 0:
            print("[ + ] No Node Exist Now.")
            
        elif self.head == self.tail:
            print("[ + ] Removing :: ", self.head.data)
            self.head = None
            self.tail = None
            print("[ + ] No Node Exist Now.")
            
        else:
            PrevNode = None
            node = self.head
            
            while node.next:
                
                PrevNode = node
                node = node.next
                
            print("[ + ] Removing :: ", self.tail.data)
            
            PrevNode.next = None
            self.tail = PrevNode
            
        self.length -= 1
        
    def prePend(self, data):
        if self.length == 0:
            self.append(data)
            return
        
        newNode = Node(data=data)
        newNode.next = self.head
        
        self.head = newNode
        self.length += 1
        
        print("[ + ] Node Added with Value :: ", data)
        
    def popFirst(self):
        print("[ + ] Removing :: ", self.head.data)
        self.head = self.head.next
        self.length -= 1
        
    def set(self, index, value):
        
        node = self.getNode(index=index)
        print("[ + ] Node Value Updated from ", node.data, end="")
        
        node.data = value
        print(" to ", node.data)

    def getNode(self, index):
        
        if index < 0 or index >= self.length:
            print("[ + ] No Node in specified Position")
            return
        if self.length > 0:
            if index == 0:
                return self.head

            if index == self.length:
                return self.tail

            count = 0
            node = self.head
        
            while node:
            
                node = node.next
                count += 1
            
                if count == index:
                    return node

    def insert(self, index, data):
        
        if self.length < index or index < 0:
            print("[ + ] No Node in specified Position")
            return
        
        if index == 0:
            return self.prePend(data=data)
        
        if index == self.length:
            return self.append(data=data)
        
        newNode = Node(data=data)
        temp = self.getNode(index=index-1)
        
        newNode.next = temp.next
        temp.next = newNode
        
        self.length += 1

        print("[ + ] Node added with Value :: ", data, " on Position :: ", index + 1)
    
    def remove(self, index):
        
        if index == 0:
            if self.length == 1:
                print("[ + ] Removing :: ", self.head.data)
                self.head = None
                self.tail = None
                self.length = 0
                return
        
        node = self.getNode(index=index-1)
        
        if node:
            print("[ + ] Removing :: ", node.data, " on Position :: ", index)
            node.next = node.next.next
            self.length -= 1
            return
        
    def printLL(self):
        if self.length == 0:
            print("[ + ] No Node Exist Now.")
        
        LL=  ""
        node = self.head
        
        table = PrettyTable()
        table.field_names = ["Index", "Node Value"]
        count = 1
        while node:
            table.add_row([count,node.data])
            node = node.next
            count+= 1
            
        print(table)
        
            
    def reverse(self):
        
        if self.length == 0:
            print("[ + ] No Node Exist Now.")
            return

        temp = self.head
        
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None
        
        for _ in range(self.length):
            
            after = temp.next
            temp.next = before
            
            before = temp
            temp = after
            
        print("[ + ] LinkedList is reversed.")

    def __str__(self) -> str:
        if self.length == 0:
            return "[ + ] No Node Exist Now."
        LL=  ""
        node = self.head
        
        while node:
            LL += "->" + str(node.data)
            node = node.next
        return LL
        
    
    def __add__(self, data: any):
        self.append(data)
    def __invert__(self) -> None:
        self.reverse()
    def has_loop(self):
        if self.length == 0:
            print('[ - ] Data is too small to have the Cycle.')
            return

        fast = self.head
        slow = self.head
        
        while(slow.next != None
              and fast != None
              and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("[ - ] Floyed Cycle Detected.")
                return
        print("[ + ] No Cycle Detected.")
        
    def remove_duplicates(self):
        if self.length <= 1:
            print("[ + ] No or Very less Nodes. Cannot Implementation Operation.")
            return
        final = set()
        prev = None
        currNode = self.head
        while currNode:
            if currNode.data in final:
                prev.next = currNode.next
                self.length -= 1
            else:
                final.add(currNode.data)
            prev = currNode
            currNode = currNode.next
        print("[ + ] No Duplicates available now.")
        pass
    def find_kth_from_end(self, k):
        if k < 1 and k > self.length:
            print("[ - ] Invalid Positional Argument. Index doesn't exist.")
        if k == 1:
            print("[ + ] Value on position", k, " from last is ::", self.tail.data)
        slow = self.head
        fast = self.head
        
        for _ in range(k):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        print("[ + ] Value on position", k, " from last is ::", slow.data)
    def partition_Reverse(self, m, n):
        
        if self.head is None:
            print("[ - ] List is Empty.")
            return
        if n > self.length or m < 0:
            print("[ - ] Positional Arguments Out of Range.")
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        for i in range(m):
            prev = prev.next
        
        current = prev.next
        
        for i in range(n-m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        self.head = dummy.next
     
    def isEmpty(self):
        if self.length == 0:
            print("[ + ] List is Empty.")
        else:
            print("[ + ] List is not Empty.")
    def length_List(self):
        print("[ + ] Total number of Members :: ", self.length)
    def partition_list(self, x):
        if not self.head:
            return None
        
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        
        while current:
            if current.data < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        
        prev2.next = None
        prev1.next = dummy2.next
        
        self.head = dummy1.next
    
"""
    isEmpty() : method returns true if the list is empty

    length() : method that returns the length of the Linked List

    findMin() : method that returns the max element

    findMax() : method that returns the min element

    count() : method that returns the occurences of an element


    tostring() : method that returns a string of all elements of the String

    copy() : method that returns the copy of the list

    clear() : method that clears the Linked List

    index() : method that returns index of a particular element

    toList() : method returns builtin List of python consisting of Elements of Linked List

    toSet() : method returns builtin Set of python consisting of Elements of Linked List

    sort() : method that sorts Linked List

    sorted() : method returns new instance of the sorted LinkedList without changing original Linked List
"""
def main():

    help = """
        BASE - OPERATIONS
            
        USAGE:
        
            DESCRIPTION                  COMMAND                              EXAMPLE
            -----------                  -------                              -------
        1)  Add Node in Last           : l+   [int_Variable]                : l+ 30
        2)  Add Node in Start          : +l   [int_Variable]                : +l 10
        3)  Add Node in Middle         : l++  [Index] [int_Variable]        : l++ 2 20
        4)  Remove Node from Last      : l-                                 : l-
        5)  Remove First Node          : -l                                 : -l
        6)  Remove Node from Middle    : l--  [Index]                       : l-- 1
        7)  Get Value of a Node        : lget [Index]                       : lget 2
        8)  Update Value of a Node     : lset [Index] [VariableNewValue]    : lset 1 45
        9)  Print all Nodes            : l                                  : l
             
        [int_Variable]   : Integer Varibale to be store in Linked List in form of Node Data
        [Index]          : Index for the Node in the Linked List is considered to be starting from 1
        ---------------------------------------------------------------------------------------------
        ADDITIONAL - OPERATIONS
        
        USAGE:
        
            DESCRIPTION                  COMMAND
            -----------                  -------
        1)  Nodes Organized View       : ll
        2)  Floyed Cycle Detection Algo: c_cl
        3)  Remove Duplicates          : rm_dup
        4)  Reverse all Node Positions : ~l
        5)  Value by Index from Last   : vi_last  [Position]
        6)  Partitioned Reverse        : p_rev [startPosition] [endPosition]
        7)  Check if List is Empty     : -e
        8)  Check length of List       : len
        9)  Partition the List with X  : pl [Value of X]
            
        [int_Variable]   : Integer Varibale to be store in Linked List in form of Node Data
        [Index]          : Index for the Node in the Linked List is considered to be starting from 1
        
        --------------------------------------------------------------------------------------------- 
        HELP/ EXIT - OPERATIONS
        
            DESCRIPTION                  COMMAND
            -----------                  ------
        1)  Clear Screen               : cls
        1)  Node Documentation         : -node--help
        2)  Linked List Documentation  : -list--help
        3)  Help                       : -h || --help
        4)  Exit                       : -e || --exit || -q || --quit  
            
    """
    one = ['l', '~l','l-','-l', 'll', 'c_cl', 'len', '-e', 'rm_dup','cls', '-h', '--help', '-e', '--exit', '-q', '--quit', '-node--help', '-list--help']
    two = ['l+','+l','l--','lget', 'vi_last', 'pl']
    three = ['l++', 'lset', 'p_rev']
    
    ll = LinkedList()
    
    command = ""
    
    print("-h or --help for Tool Usage Support")
    
    while True:
        
        command = input("Command > ")
        if command == '':
            pass
        else:
            command = command.split(" ")
            if (command[0] in one) and len(command) == 1:
                if command[0] == "l":
                    print(ll)
                elif command[0] == "~l":
                    ~ll
                elif command[0] == "l-":
                    ll.pop()
                elif command[0] == "len":
                    ll.length_List()    
                elif command[0] == "-l":
                    ll.popFirst()
                elif command[0] == '-e':
                    ll.isEmpty()
                elif command[0] == 'll':
                    ll.printLL()
                elif command[0] == 'c_cl':
                    ll.has_loop()    
                elif command[0] == 'rm_dup':
                    ll.remove_duplicates()
                elif command[0] == 'cls':
                    os.system('cls')
                elif command[0] == '-node--help':
                    print(Node.__doc__)
                elif command[0] == '-list--help':
                    print(LinkedList.__doc__)
                elif command[0] == "-h" or command[0] == "--help":
                    print(help)
                elif command[0] in ['-e', '--exit', '-q', '--quit']:
                    exit()
            elif (command[0] in two) and len(command) == 2:
                try:
                    command[1] = int(command[1])
                    if command[0] == "l+":
                        ll + command[1]
                    elif command[0] == "+l":
                        ll.prePend(command[1])
                    elif command[0] == "l--":
                        ll.remove(command[1]-1)
                    elif command[0] == "lget":
                        print(ll.getNode(command[1]-1).data)
                    elif command[0] == "vi_last":
                        ll.find_kth_from_end(command[1])
                    elif command[0] == "pl":
                        ll.partition_list(command[1])
                except:
                    print("[ - ] Positional Argument incorrent.")
                    continue
            elif (command[0] in three) and len(command) == 3:
                try:
                    command[1] = int(command[1])
                    command[2] = int(command[2])
                    if command[0] == "l++":
                        ll.insert(int(command[1])-1,int(command[2]))
                    elif command[0] == "lset":
                        ll.set(int(command[1])-1, int(command[2]))
                    elif command[0] == "p_rev":
                        ll.partition_Reverse(int(command[1])-1, int(command[2]-1))
                except:
                    print("[ - ] Positional Argument incorrent.")
                    continue
            else:
                print("[ - ] Some Positional Arguments Missing or Incorrent.\n[ - ] Please type -h or --help for command and Attribute Help.")

if __name__ == "__main__":
    main()
