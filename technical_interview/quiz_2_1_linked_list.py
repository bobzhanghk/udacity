"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        index = 1
        current = self.head
        if self.head and position > 0:
            while index < position:
                if current.next:
                    current = current.next
                    index += 1
                else:
                    return None
            return current
        else:
            return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        index = 1
        last = None
        current = self.head
        if self.head and new_element:
            if position > 1:
                while index < position:
                    if current.next:
                        last = current 
                        current = current.next
                        index += 1
                last.next = new_element
                new_element.next = current
            elif position == 1:
                new_element.next = current
                self.head = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        index = 1
        lase = None
        current = self.head
        if self.head and value:
            while current.value != value:
                if current.next:
                    last = current 
                    current = current.next
                    index += 1
                else:
                    return -1
            if index > 1:
                last.next = current.next
            else:
                self.head = current.next
            return index
        else:
            return -1

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ((ll.head.next.next.value) == 3)
# Should also print 3
print ((ll.get_position(3).value) == 3)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ((ll.get_position(3).value) == 4)

# Test delete
ll.delete(1)
# Should print 2 now
print ((ll.get_position(1).value) == 2)
# Should print 4 now
print ((ll.get_position(2).value) == 4)
# Should print 3 now
print ((ll.get_position(3).value) == 3)