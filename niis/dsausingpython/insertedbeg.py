def insert_beg(self, data):
    cur = Node(data)

    if self.head is None:
        self.head = cur
        cur.next = cur
        cur.prev = cur
    else:
        last = self.head.prev

        cur.next = self.head
        cur.prev = last

        last.next = cur
        self.head.prev = cur

        self.head = cur

    print("Inserted at beginning")