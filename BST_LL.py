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


def searchBT(rootNode , nodeValue):
    if rootNode is None:
        return 'Binary Tree is Empty .'

    elif rootNode.data == nodeValue:
        print("Found")

    elif nodeValue > rootNode.data:
        if rootNode.rightChild.data == nodeValue :
            print("Found")
        else:
            searchBT(rootNode.rightChild , nodeValue)

    elif nodeValue < rootNode.data:
        if rootNode.leftChild.dataa == nodeValue:
            print("Found")
        else:
            searchBT(rootNode.leftChild , nodeValue)


def minValueNode(rootNode):
    curr = rootNode
    while curr.leftChild is None:
        curr = curr.leftChild
    return curr



def deleteNode(rootNode , nodeValue):
    if rootNode is None :
        return rootNode
    
    elif nodeValue < rootNode.data :
        rootNode.leftChild = deleteNode(rootNode.leftChild , nodeValue)

    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild , nodeValue)

    else:
        if rootNode.leftChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild , temp.data)

    return rootNode

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
