class BinaryTree:
    def __init_(self , size):
        self.customList = size * [None]
        self.LastUsedIndex = 0
        self.maxSize = size

    def insertNode(self , value):
        
        if self.LastUsedIndex+1 == self.maxSize:
            return "Tree is full"
        else:
            self.customList[self.LastUsedIndex + 1] = value
            self.LastUsedIndex += 1
            return "Value inserted successfully"