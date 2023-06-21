import random


# O(1) Time complexity for all methods
# Without duplication
class Store:
    def __init__(self) -> None:
        self.arr = list()
        self.obj = dict()

    def insert(self, value):
        if value in self.obj:
            return
        self.arr.append(value)
        self.obj[value] = len(self.arr) - 1

    def remove(self, value):
        if value not in self.obj:
            return
        last_val = self.arr[-1]
        ind = self.obj[value]
        self.arr[-1] = value
        self.arr[ind] = last_val
        self.obj[last_val] = ind
        self.arr.pop()
        del self.obj[value]

    def choose_random(self):

        if len(self.arr) > 0:
            return random.choice(self.arr)
        # else: return ''


# With Duplication
class NotDuplicateStore:
    def __init__(self) -> None:
        self.arr = list()
        self.obj = dict()

    def insert(self, value):
        self.arr.append(value)
        if value in self.obj:
            self.obj[value].append(len(self.arr) - 1)
        else:
            self.obj[value] = [len(self.arr) - 1]

    def remove(self, value):
        if value in self.obj:
            ind = self.obj[value][-1]
            last_value = self.arr[-1]
            self.arr[-1] = self.arr[ind]
            self.arr[ind] = last_value
            self.arr.pop()
            if len(self.obj[value]) > 1:
                self.obj[value].pop()
            else:
                del self.obj[value]

    def choose_random(self):
        if len(self.arr) > 0:
            return random.choice(self.arr)
