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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return (getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild))

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild , nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild , nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)

    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)

    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)

    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode