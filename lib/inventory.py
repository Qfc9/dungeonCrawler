# Handling inventories
class Inventory():
    def __init__(self):
        self.contains = []

    # add an item to the self.contains list
    def add(self, newItem):
        if newItem is None:
            return
        self.contains.append(newItem)

    # remove and return item in the self.contains list
    def takeOut(self, idx):
        return self.contains.pop(idx)
