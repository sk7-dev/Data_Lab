from random import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        self.list[self.dict[val]], self.list[-1] = self.list[-1], self.list[self.dict[val]]
        self.dict[self.list[self.dict[val]]] = self.dict[val]
        del self.dict[self.list[-1]]
        self.list.pop(-1)
        return True

    def getRandom(self) -> int:
        return self.list[int((random() * len(self.list)))]