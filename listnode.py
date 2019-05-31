#linked list node for hashes (linked list so can handle collisions)
class listnode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def addNext(self, nextItem):
        self.next = nextItem
    def addData(self, data):
        self.data = data
    def hasNext(self):
        if self.next == None:
            return False
        return True
    def hasData(self):
        if self.data == None:
            return False
        return True