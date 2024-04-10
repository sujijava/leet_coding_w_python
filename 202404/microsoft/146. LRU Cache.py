class LRUCache(dict):
    def __init__(self, cap):
        self.remaining = cap
        
    def get(self, key):
        if key not in self:
            return -1
        val = self.pop(key) # pop and re-insert to keep the order
        self[key] = val
        return val
        
    def put(self, key, value):
        if key in self:
            self.pop(key)
        else:
            if self.remaining > 0: 
                self.remaining -= 1
            else: 
                self.pop(next(iter(self))) # cache is full, remove least recently used key which is the first key 
        self[key] = value
