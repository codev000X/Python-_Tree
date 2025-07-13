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

    def searchNode(self, node):
        return 'Success' if node in self.customList else 'Not found.'

    def preOrderTraversal(self , index):
        if index > self.LastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTrveral(index*2 + 1)

    def inOrderTraveral(self , index):
        if index > self.LastUsedIndex:
            return
        self.preOrderTraversal(index*2)
        print(self.customList[index])
        self.preOrderTrveral(index*2 + 1)

    def postOrderTraversal(self , index):
        if index > self.LastUsedIndex:
            return
        self.preOrderTraversal(index*2)
        self.preOrderTrveral(index*2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self , index):
        for i in range(index , self.lastUsedIndex + 1):
            print(self.customlist[i])