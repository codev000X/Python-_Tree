from LinkedList__Queue import Queue
class TreeNode:
    def __init__(self , data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootNode):
    if not  rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode , nodeValue):
    if not rootNode:
        return 'Binary tree does not exist'
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return f'Node with value {nodeValue} found'
            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)
        return f'Node with value {nodeValue} does not exist in the binary tree'

def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return 'Node inserted successfully'
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if not root.value.leftChild:
                customQueue.enqueue(rootNode.value.leftChild)
            else:
                customQueue.leftChild(newNode)
                return 'Node inserted successfully'
            if not root.value.rightChild:
                customQueue.enqueue(rootNode.value.rightChild)
            else:
                customQueue.rightChild(newNode)
                return 'Node inserted successfully'

