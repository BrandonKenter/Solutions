from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.index_num = {}
        self.num_indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_num:
            to_remove = self.index_num[index]
            self.num_indices[to_remove].discard(index)
        
        if number not in self.num_indices:
            self.num_indices[number] = SortedSet()

        self.num_indices[number].add(index)
        self.index_num[index] = number

    def find(self, number: int) -> int:
        if number in self.num_indices and len(self.num_indices[number]) > 0:
            return self.num_indices[number][0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)