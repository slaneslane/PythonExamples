# hashmap.py
# based on: https://www.youtube.com/watch?v=9HFbhPscPU0

class HashMap(object):

    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        # still doesn't exists:
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            # exists so replace with a new value:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # key doesn't exists yet for this key_hash location
            # so append a new pair to it:
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def display(self):
        print('----HashMap----')
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()
h.add('Bob', '234-2342')
h.add('Ming', '234-2433')
h.add('Ming', '333-2333')
h.add('Ankit', '278-2342')
h.add('Aditya', '200-2342')
h.add('Alicia', '634-2342')
h.add('Mike', '534-2342')
h.add('Aditya', '000-2342')
h.display()
h.delete('Bob')
h.display()
print('Ming:' + h.get('Ming'))
