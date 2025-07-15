from LinkedList__Queue import Queue

class AVLNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        currentNode = queue.dequeue()
        print(currentNode.data)
        if currentNode.left:
            queue.enqueue(currentNode.left)
        if currentNode.right:
            queue.enqueue(currentNode.right)    

def searchNode(rootNode , nodeValue):
    if rootNode.data == nodeValue :
        print("The value is Found")
    elif nodeValue < rootNode.data :
        if rootNode.leftChild.data == nodeValue :
            print ('The value is found.')
        else:
            searchNode(rootNode.leftChild , nodeValue)
    else:
        if rootNode.rightChild.daata == nodeValue:
            print('The value is found')
        else:
            searchNode(rootNode.rightChild , nodeValue)
