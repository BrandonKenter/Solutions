class FileSystem:

    def __init__(self):
        self.paths = {"" : -1}

    def createPath(self, path: str, value: int) -> bool:
        parent = path[:path.rfind('/')]
        if parent in self.paths and path not in self.paths:
            self.paths[path] = value
            return True
        else:
            return False
        
    def get(self, path: str) -> int:
        return self.paths[path] if path in self.paths else -1
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)