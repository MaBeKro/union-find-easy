class Item:
    def __init__(self, val=None, rep=None):
        self.rep = rep if rep else self
        self.val = val
        self.weight = 1

    def find(self):
        if self.rep == self:
            return self
        else:
            self.rep = self.rep.find()
            return self.rep

    def union(self, other):
        r1 = self.find()
        r2 = other.find()
        if r1 == r2:
            return
        if r1.weight < r2.weight:
            r1, r2 = r2, r1
        r2.rep = r1
        r1.weight += r2.weight
    
    def member_count(self):
        return self.find().weight

    def __str__(self):
        return f"Item(rep={self.rep.__repr__()}, val={self.val}, weight={self.weight})"

def Union(*items):
    if items:
        it = items[0]
        for i in items[1:]:
            it.union(i)
