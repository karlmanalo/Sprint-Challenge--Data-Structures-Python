class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.storage = []
        # Define list with n None elements, where n is the capacity
        self.storage = [None] * capacity
        self.index = 0

    def append(self, item):
        # self.storage.append(item)
        # if len(self.storage) > self.capacity:
        #   self.storage = self.storage[1:]
        # Can't do this because it doesn't replace oldest value at 
        # correct index position. It deletes the oldest value, but 
        # inserts the newest value at the end of the list.
        self.storage[self.index] = item
        self.index += 1
        # Resets index when capacity is met
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        # List comprehension to exclude None values
        return [item for item in self.storage if item != None]