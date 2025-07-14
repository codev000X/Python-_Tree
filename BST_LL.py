from LinkedList__Queue import Queue

class BSTNode:
    def __init__(self , data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertBST(rootNode , nodeValue):
    if rootNode == None :
        rootNode.data = BSTNode(nodeValue)
    elif nodeValue > rootNode.data:
        if rootNode.rightChild == None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertBST(rootNode.rightChild , nodeValue)
    else:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertBST(rootNode.leftChild , nodeValue)
    return 'Node added Succefully .'

def preOrderTraversal(rootNode):
    if rootNode is None:
        return 'Tree is Empty .'
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return 'Tree is Empty .'
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return 'Tree is Empty .'
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data) 

def levelOrderTraversal(rootNode):
    if rootNode is None:
        return 'Tree is Empty .'

    customQueue = Queue()
    customQueue.enqueue(rootNode)

    while not(customQueue.isEmpty()):
        rootNode = customQueue.dequeue()
        print(rootNode.data)

        if rootNode.leftChild is not None:
            customQueue.enqueue(rootNode.leftChild)
        if rootNode.rightChild is not None:
            customQueue.enqueue(rootNode.rightChild)