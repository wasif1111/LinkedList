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


def main():
    
    help = """
        LINKED LIST
            
        Usage:
        1)  Add Node in Last           : l+   [int_Variable]
        2)  Add Node in Start          : +l   [int_Variable]
        3)  Add Node in Middle         : l++  [Index] [int_Variable]
        4)  Remove Node from Last      : l-   
        5)  Remvoe First Node          : -l   
        6)  Remove Node from Middle    : l--  [Index]
        7)  Get Value of a Node        : lget [Index]
        8)  Update Value of a Node     : lset [Index] [VariableNewValue]
        9)  Print all Nodes            : l  
        10) Reverse all Node Positions : ~l
             
        [int_Variable]   : Integer Varibale to be store in Linked List in form of Node Data
        [Index]          : Index for the Node in the Linked List is considered to be starting from 1
             
        Additional Operations:
        1)  Nodes Organized View       :       prettyll
        2)  Node Documentation         :       -node--help
        3)  Linked List Documentation  :       -list--help
        4)  Help                       :       -h || --help
        5)  Exit                       :       -e || --exit || -q || --quit  
            
    """
    one = ['l', '~l','l-','-l', 'prettyll', '-h', '--help', '-e', '--exit', '-q', '--quit', '-node--help', '-list--help']
    two = ['l+','+l','l--','lget']
    three = ['l++', 'lset']
    
    ll = LinkedList()
    
    command = ""
    
    print("-h or --help for Tool Usage Support")
    
    while True:
        
        command = input("Base > ")
        command = command.split(" ")
        
        if (command[0] in one) and len(command) == 1:
            
            if command[0] == "l":
                print(ll)
                
            elif command[0] == "~l":
                ~ll
            
            elif command[0] == "l-":
                ll.pop()
                
            elif command[0] == "-l":
                ll.popFirst()    
                
            elif command[0] == 'prettyll':
                ll.printLL()
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
            except:
                
                print("[ - ] Positional Argument incorrent.")
                continue
        else:
            print("[ - ] Some Positional Arguments Missing or Incorrent.\n[ - ] Please type -h or --help for command and Attribute Help.")
    pass

if __name__ == "__main__":
    main()