from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity is self.storage.length:
            if self.current == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                self.current.insert_after(item)
                self.storage.length += 1
                self.current = self.current.next
                self.storage.delete(self.current.next)
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head

        if self.storage.length == 1:
            list_buffer_contents.append(self.storage.head.value)
        elif self.storage.length > 1:
            while node.next:
                list_buffer_contents.append(node.value)
                node = node.next
            list_buffer_contents.append(node.value)
        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
