class MyHashSet:

    def __init__(self):
        self.n = 1024
        self.container = [[] for _ in range(self.n)]
    def _hash(self, key):
        return hash(key) % self.n    

    def add(self, key: int) -> None:
        i = self._hash(key)
        if key not in self.container[i]:
            self.container[i].append(key)
        

    def remove(self, key: int) -> None:
        i = self._hash(key)
        if key in self.container[i]:
            self.container[i].remove(key)
        

    def contains(self, key: int) -> bool:
        i = self._hash(key)
        return key in self.container[i]
