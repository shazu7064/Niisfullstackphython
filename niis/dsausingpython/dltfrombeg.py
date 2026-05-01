def delete_beg(self):
    if self.head is None:
        print("No element")
        return

    # Case: Only one node
    if self.head.next == self.head:
        print("Deleted:", self.head.data)
        self.head = None
        return

    # Get last node
    last = self.head.prev

    print("Deleted:", self.head.data)

    # Move head forward
    self.head = self.head.next

    # Fix links
    self.head.prev = last
    last.next = self.head